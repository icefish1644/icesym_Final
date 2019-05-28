/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*- */
/*
 * sim-c
 * Copyright (C) Juan Marcelo Gimenez 2009 <jmarcelogimenez@gmail.com>
 * 
 * sim-c is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the
 * Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * sim-c is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License along
 * with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#include "simulator.h"
#include <math.h>
#include <limits.h>
#include <sstream>
#include <vector>
#include <sys/types.h>
#include <sys/stat.h>
#include <stdio.h>
#include <stdlib.h>

double modulo(double x, double y){
	return x-y*floor(x/y);
}

/**
   \brief Simulator's costructor
*/
Simulator::Simulator(double dt, double tf, int nrpms, vector<double> rpms, 
					 vector<double> Xn, vector<double> Xn1, int ntubes,
					 int ncyl, int ntank, int njunc, int iter_sim1d, int nsave,
					 int nappend, double dtheta_rpm, int inicia, double Courant,
					 double ga, int viscous_flow, int heat_flow, double R_gas,
					 double theta_cycle, int ncycles, int engine_type, 
					 char* filein_state,char* filesave_state,char* filein_spd,
					 char* filesave_spd, char* folder_name,
					 vector<int> ig_order, vector<Cylinder> cylinders,
					 vector<Tube> tubes, vector<Junction> junctions,
					 vector<Tank> tanks, int natm, 
					 vector<Atmosphere> atmospheres, 
					 int get_state, int calc_engine_data, 
					 int use_global_gas_prop, double ga_intake, 
					 double ga_exhaust){
	this->dt = dt;
	this->tf = tf;
	this->nrpms = nrpms;
	this->rpms = rpms;
	this->Xn = Xn;
	this->Xn1 = Xn1;
	this->ntubes = ntubes;
	this->ncyl = ncyl;
	this->ntank = ntank;
	this->njunc = njunc;
	this->natm = natm;
	this->iter_sim1d = iter_sim1d;
	this->nsave = nsave;
	this->nappend = nappend;
	this->dtheta_rpm = dtheta_rpm;
	this->inicia = inicia;
	this->Courant = Courant;
	this->ga = ga;
	this->viscous_flow = viscous_flow;
	this->heat_flow = heat_flow;
	this->R_gas = R_gas;
	this->theta_cycle = theta_cycle;
	this->ncycles = ncycles;
	this->engine_type = engine_type;
	strcopy(this->filein_state,filein_state);
	strcopy(this->filesave_state,filesave_state);
	strcopy(this->filein_spd,filein_spd);
	strcopy(this->filesave_spd,filesave_spd);
	strcopy(this->folder_name,folder_name);
	this->ig_order = ig_order;
	this->cylinders = cylinders;
	this->tubes = tubes;
	this->junctions = junctions;
	this->tanks = tanks;	
	this->atmospheres = atmospheres;
	this->get_state = get_state;
	this->calc_engine_data = calc_engine_data;
	this->use_global_gas_prop = use_global_gas_prop;
	this->ga_intake = ga_intake;
	this->ga_exhaust = ga_exhaust;

	this->irpm = 0;

	makeSimulation();
}

/**
   \brief makes the Global State and the relationships between components
*/
void Simulator::makeSimulation(){
	unsigned int iXn = 0;
	char str_cylinder[9]	= "cylinder"; 
	char str_tube[5]		= "tube"; 
	char str_tank[5]		= "tank";
	char str_junction[9]	= "junction"; 
	
	//cout<<"en make simulation"<<endl;
	if(get_state==1)
		readState();
	// cout<<"apasa read state"<<endl;
	for(int k=0;k<natm;k++){
		atmospheres[k].Make(Xn,iXn,get_state);
	}
	// cout<<"hizo atm"<<endl;

	dataSim globalData;
	if(get_state==2)
		makeStruct(globalData);
	
	// cout<<"init cylinders"<<endl;
	double atm[3] = {Xn[0],Xn[1],Xn[2]};
	initialize_cylinders(&(this->ncyl));
	// cout<<"pasa init cylinders"<<endl;
	for(int k=0;k<ntubes;k++){
		if(get_state==2)
			tubes[k].calculate_state(atm,globalData);
		tubes[k].Make(Xn,iXn,get_state);
		tubes[k].dt_max = this->dt;
		tubes[k].itube = k;
	}
	// cout<<"hizo tubes"<<endl;
	
	for(int k=0;k<ncyl;k++){
		for(unsigned int i=0;i<cylinders[k].nvi;i++){
			Tube* tubeRef = &(tubes[cylinders[k].intake_valves[i].tube]);
			cylinders[k].intake_valves[i].dx_tube     = &(tubeRef->hele[tubeRef->nnod-2]);
			cylinders[k].intake_valves[i].Area_tube   = &(tubeRef->Area[tubeRef->nnod-1]);
			cylinders[k].intake_valves[i].dAreax_tube = &(tubeRef->dAreax[tubeRef->nnod-1]);
			cylinders[k].intake_valves[i].twall_tube  = &(tubeRef->twall[tubeRef->nnod-1]);
		}
		for(unsigned int i=0;i<cylinders[k].nve;i++){
			Tube* tubeRef = &(tubes[cylinders[k].exhaust_valves[i].tube]);
			cylinders[k].exhaust_valves[i].dx_tube     = &(tubeRef->hele[0]);
			cylinders[k].exhaust_valves[i].Area_tube   = &(tubeRef->Area[0]);
			cylinders[k].exhaust_valves[i].twall_tube  = &(tubeRef->twall[0]);
			cylinders[k].exhaust_valves[i].dAreax_tube = &(tubeRef->dAreax[0]);
		}
		
	}
	for(int k=0;k<ncyl;k++){
		int icyl = k+1;
		cylinders[k].initFortran(icyl,globalData);
		if(get_state==2)
			cylinders[k].calculate_state(atm,globalData);
		// cout<<"pasa el get state"<<endl;
		cylinders[k].Make(Xn,iXn,get_state);
	}

	// cout<<"hizo cyl"<<endl;
	for(int k=0;k<njunc;k++){
		if(get_state==2)
			junctions[k].calculate_state(atm,globalData);
		junctions[k].Make(Xn,iXn,get_state);
	}

	// cout<<"hizo junc"<<endl;
	for(int k=0;k<ntank;k++){
		if(get_state==2)
			tanks[k].calculate_state(atm,globalData);
		tanks[k].Make(Xn,iXn,get_state);
	}

	// cout<<"hizo tank"<<endl;
	Xn1.resize(Xn.size());
	/*
	  Por cada tube, solo tengo 2 estados de referencia (left y right), tomo el 
	  correspondiente dependiendo de que objeto tenga a los lados
	  Si es junction, depende del orden de los nodos de la union
	  Si es cylinder, depende si es de admision o escape, y su ubicacion alli
	  Si es tube, tank y atmosphere es trivial
	*/
	for(int k=0;k<ntubes;k++){
		if(strcomp(tubes[k].tleft,str_junction)){
			Junction juncRef = junctions[tubes[k].nleft];
			unsigned int nodRef;
			for(nodRef=0;nodRef<juncRef.nnod;nodRef++){
				if(juncRef.node2tube[nodRef] == k)
					break;
			}
			for(unsigned int i=0;i<juncRef.ndof;i++)
				tubes[k].i_state.push_back(juncRef.i_state[nodRef*juncRef.ndof + i]);
		}
		else{
			if(strcomp(tubes[k].tleft,str_cylinder)){
				Cylinder cylRef = cylinders[tubes[k].nleft];
				unsigned int nodRef;
				for(nodRef=0;nodRef<cylRef.nve;nodRef++){
					if(cylRef.exhaust_valves[nodRef].tube == k)
						break;
				}
				for(unsigned int i=0;i<cylRef.ndof;i++)
					tubes[k].i_state.push_back(cylRef.i_state[(cylRef.nnod-cylRef.nve+nodRef)*cylRef.ndof + i]);
			}
			else{
				if(strcomp(tubes[k].tleft,str_tube)){
					Tube refTube = tubes[tubes[k].nleft];
					for(unsigned int i=0;i<refTube.ndof;i++)
						tubes[k].i_state.push_back(refTube.i_state[(refTube.nnod-1)*refTube.ndof + i]);
				}
				else{
					if(strcomp(tubes[k].tleft,str_tank)){
						Tank tankRef = tanks[tubes[k].nleft];
						unsigned int nodRef;
						for(nodRef=0;nodRef<tankRef.exh2tube.size();nodRef++){
							if(tankRef.exh2tube[nodRef] == k)
								break;
						}
						for(unsigned int i=0;i<tankRef.ndof;i++)
							tubes[k].i_state.push_back(tankRef.i_state[(tankRef.int2tube.size()+nodRef+1)*tankRef.ndof + i]);
					}
					else{
						Atmosphere atmRef = atmospheres[tubes[k].nleft];
						for(unsigned int i=0;i<atmRef.ndof;i++)
							tubes[k].i_state.push_back(atmRef.i_state[i]);
					}
				}
			}
		}
		if(strcomp(tubes[k].tright,str_junction)){
			Junction juncRef = junctions[tubes[k].nright];
			unsigned int nodRef;
			for(nodRef=0;nodRef<juncRef.nnod;nodRef++){
				if(juncRef.node2tube[nodRef] == k)
					break;
			}
			for(unsigned int i=0;i<juncRef.ndof;i++)
				tubes[k].i_state.push_back(juncRef.i_state[nodRef*juncRef.ndof + i]);
		}
		else{
			if(strcomp(tubes[k].tright,str_cylinder)){
				Cylinder cylRef = cylinders[tubes[k].nright];
				unsigned int nodRef;
				for(nodRef=0;nodRef<cylRef.nvi;nodRef++){
					if(cylRef.intake_valves[nodRef].tube == k)
						break;
				}
				for(unsigned int i=0;i<cylRef.ndof;i++){
					int num = cylRef.i_state[(cylRef.nnod-cylRef.nvi-cylRef.nve+nodRef)*cylRef.ndof + i];
					tubes[k].i_state.push_back(num);
				}
			}
			else{
				if(strcomp(tubes[k].tright,str_tube)){
					Tube refTube = tubes[tubes[k].nright];
					for(unsigned int i=0;i<refTube.ndof;i++)
						tubes[k].i_state.push_back(refTube.i_state[i]);
				}
				else{
					if(strcomp(tubes[k].tright,str_tank)){
						Tank tankRef = tanks[tubes[k].nright];
						unsigned int nodRef;
						for(nodRef=0;nodRef<tankRef.int2tube.size();nodRef++){
							if(tankRef.int2tube[nodRef] == k)
								break;
						}
						for(unsigned int i=0;i<tankRef.ndof;i++)
							tubes[k].i_state.push_back(tankRef.i_state[(nodRef + 1)*tankRef.ndof  + i]);
					}
					else{
						Atmosphere atmRef = atmospheres[tubes[k].nright];
						for(unsigned int i=0;i<atmRef.ndof;i++)
							tubes[k].i_state.push_back(atmRef.i_state[i]);
					}
				}
			}
		}
	}
	/*
	  debemos tomar como estado de referencia cada relacion valve-tube
	  toma el primer nodo del tube si es "exhaust"
	  toma el ultimo nodo del tube si es "intake"
	*/
	// cout<<"empieza make cylinder"<<endl;
	for(int k=0;k<ncyl;k++){
		for(unsigned int i=0;i<cylinders[k].nvi;i++){
			Tube* tubeRef = &(tubes[cylinders[k].intake_valves[i].tube]);
			for(unsigned int j=0;j<tubeRef->ndof;j++){
				cylinders[k].i_state.push_back(tubeRef->i_state[(tubeRef->nnod-1)*tubeRef->ndof + j]);
			}
		}
		for(unsigned int i=0;i<cylinders[k].nve;i++){
			Tube* tubeRef = &(tubes[cylinders[k].exhaust_valves[i].tube]);
			for(unsigned int j=0;j<tubeRef->ndof;j++){
				cylinders[k].i_state.push_back(tubeRef->i_state[j]);
			}
		}
		if(this->engine_type==2){
			/*
			  For the MRCVC engine we add two reference nodes. The first node
			  corresponds to the 'leading' chamber and the second node to
			  the 'trailing' chamber
			*/
			unsigned int lcyl,tcyl;
			lcyl = (((k-1)%ncyl)+ncyl)%ncyl;
			tcyl = (((k+1)%ncyl)+ncyl)%ncyl;
			for(unsigned int j=0;j<cylinders[k].ndof;j++)
				cylinders[k].i_state.push_back(cylinders[lcyl].i_state[j]);
			for(unsigned int j=0;j<cylinders[k].ndof;j++)
				cylinders[k].i_state.push_back(cylinders[tcyl].i_state[j]);
		}
	}
	/* 
	   Junction solo se conecta a tubes. 
	   Por cada nodo hay un estado de referencia, que es el ultimo o primero del pipe, dependiendo de donde esté el tube.
	*/
	//cout<<"empieza make junction"<<endl;
	for(int k=0;k<njunc;k++){
		for(unsigned int i=0;i<junctions[k].nnod;i++){
			unsigned int iTube = junctions[k].node2tube[i];
			bool left = false; // tube a la izquierda o no
			if((int)tubes[iTube].nleft == k && strcomp(tubes[iTube].tleft,str_junction)) //si esta junction esta a la izquierda del tube
				left = true;
			for(unsigned int j=0;j<tubes[iTube].ndof;j++){
				if(left)
					junctions[k].i_state.push_back(tubes[iTube].i_state[j]);
				else
					junctions[k].i_state.push_back(tubes[iTube].i_state[(tubes[iTube].nnod-1)*tubes[iTube].ndof + j]);
			}   
			if(left){
				junctions[k].dx_tube[i]     = &(tubes[iTube].hele[0]);
				junctions[k].Area_tube[i]   = &(tubes[iTube].Area[0]);
				junctions[k].twall_tube[i]  = &(tubes[iTube].twall[0]);
				junctions[k].dAreax_tube[i] = &(tubes[iTube].dAreax[0]);
			}
			else{
				junctions[k].dx_tube[i]     = &(tubes[iTube].hele[tubes[iTube].nnod-1]);
				junctions[k].Area_tube[i]   = &(tubes[iTube].Area[tubes[iTube].nnod-1]);
				junctions[k].twall_tube[i]  = &(tubes[iTube].twall[tubes[iTube].nnod-1]);
				junctions[k].dAreax_tube[i] = &(tubes[iTube].dAreax[tubes[iTube].nnod-1]);
			}
		}
	}
	/*
	  tank tiene su nodo y n nodos que representan las conexiones a tubos, por lo tanto n estados de referencia
	*/
	//cout<<"empieza make tank"<<endl;
	for(int k=0;k<ntank;k++){
		for(unsigned int i=0;i<tanks[k].int2tube.size();i++){
			Tube* tubeRef = &(tubes[tanks[k].int2tube[i]]);
			for(unsigned int j=0;j<tubeRef->ndof;j++){
				tanks[k].i_state.push_back(tubeRef->i_state[(tubeRef->nnod-1)*tubeRef->ndof + j]);
			}
			tanks[k].Area_tube[i]   = &(tubeRef->Area[tubeRef->nnod-1]);
			tanks[k].twall_tube[i]  = &(tubeRef->twall[tubeRef->nnod-1]);
			tanks[k].dAreax_tube[i] = &(tubeRef->dAreax[tubeRef->nnod-1]);
		}
		for(unsigned int i=0;i<tanks[k].exh2tube.size();i++){
			Tube* tubeRef = &(tubes[tanks[k].exh2tube[i]]);
			for(unsigned int j=0;j<tubeRef->ndof;j++){
				tanks[k].i_state.push_back(tubeRef->i_state[j]);
			}
			tanks[k].Area_tube[i+tanks[k].int2tube.size()]   = &(tubeRef->Area[0]);
			tanks[k].twall_tube[i+tanks[k].int2tube.size()]  = &(tubeRef->twall[0]);
			tanks[k].dAreax_tube[i+tanks[k].int2tube.size()] = &(tubeRef->dAreax[0]);
		}
	}
	createDir(false);
}

/**
   \brief Changes the reference state for tubes
   Useful for the simulation of the MRCVC engine
   and others rotary engines
*/
void Simulator::change_ref_state_tubes(double theta){

	unsigned int nvi=0,nve=0;

	for(int i=0;i<ncyl;i++){
		double theta_cyl = modulo(theta+cylinders[i].theta_0,
								  theta_cycle);
		for(unsigned int j=0;j<cylinders[i].nvi;j++){
			double IVO = cylinders[i].intake_valves[j].angle_V0;
			double IVC = cylinders[i].intake_valves[j].angle_VC;
			if(modulo(theta_cyl-IVO,theta_cycle) >= 0. &&
			   modulo(theta_cyl-IVO,theta_cycle) <= modulo(IVC-IVO,theta_cycle)){
				nvi++;
				int itube =	cylinders[i].intake_valves[j].tube;
				// We must to erase the last ndof elements of i_state...
				for(unsigned int k=0;k<cylinders[i].ndof;k++)
					tubes[itube].i_state.pop_back();
				// ...and assign the new ones
				for(unsigned int k=0;k<cylinders[i].ndof;k++){
					int num = cylinders[i].i_state[(cylinders[i].nnod-cylinders[i].nvi-
													cylinders[i].nve+j)*cylinders[i].ndof + k];
					tubes[itube].i_state.push_back(num);
				}
				// cout<<"intake cylinder: "<<i<<endl;
			}
		}
		if(nvi==cylinders[0].nvi) break;
	}

	for(int i=0;i<ncyl;i++){
		double theta_cyl = modulo(theta+cylinders[i].theta_0,
								  theta_cycle);
		for(unsigned int j=0;j<cylinders[i].nve;j++){
			double EVO = cylinders[i].exhaust_valves[j].angle_V0;
			double EVC = cylinders[i].exhaust_valves[j].angle_VC;
			if(modulo(theta_cyl-EVO,theta_cycle) >= 0. &&
			   modulo(theta_cyl-EVO,theta_cycle) <= modulo(EVC-EVO,theta_cycle)){
				nve++;
				int itube =	cylinders[i].exhaust_valves[j].tube;
				// We must to erase the elements of i_state corresponding 
				// to the 'old' exhaust valve...
				for(unsigned int k=0;k<cylinders[i].ndof;k++)
					tubes[itube].i_state.erase(tubes[itube].i_state.end()-cylinders[i].ndof-1);
				for(unsigned int k=0;k<cylinders[i].ndof;k++){
					int num = cylinders[i].i_state[(cylinders[i].nnod-cylinders[i].nve+j)
												   *cylinders[i].ndof + k];
					// ...and assign the new ones
					tubes[itube].i_state.insert(tubes[itube].i_state.end()-cylinders[i].ndof, num);
				}
				// cout<<"exhaust cylinder: "<<i<<endl;
			}
		}
		if(nve==cylinders[0].nve) break;
	}
}

/**
   \brief Overwrites the state at the end points of
   a pipe connected with a valve.
   By the time, is only used for the simulation of the MRCVC 
   engine
*/
void Simulator::correct_state_tubes(double theta){

	unsigned int nvi=0,nve=0;

	for(int i=0;i<ncyl;i++){
		double theta_cyl = modulo(theta+cylinders[i].theta_0,
								  theta_cycle);
		unsigned int ndof = cylinders[i].ndof;
		for(unsigned int j=0;j<cylinders[i].nvi;j++){
			double IVO = cylinders[i].intake_valves[j].angle_V0;
			double IVC = cylinders[i].intake_valves[j].angle_VC;
			if(modulo(theta_cyl-IVO,theta_cycle) >= 0. &&
			   modulo(theta_cyl-IVO,theta_cycle) <= modulo(IVC-IVO,theta_cycle)){
				nvi++;
				int itube =	cylinders[i].intake_valves[j].tube;
				unsigned int nnod_tube = tubes[itube].nnod;
				int nod_ist = cylinders[i].nnod-cylinders[i].nvi-
					cylinders[i].nve+j;
				for(unsigned int k=0;k<ndof;k++)
					Xn1[tubes[itube].i_new_state[(nnod_tube-1)*ndof+k]] = 
						cylinders[i].new_state[nod_ist*ndof+k];
			}
		}
		if(nvi==cylinders[0].nvi) break;
	}

	for(int i=0;i<ncyl;i++){
		double theta_cyl = modulo(theta+cylinders[i].theta_0,
								  theta_cycle);
		unsigned int ndof = cylinders[i].ndof;
		for(unsigned int j=0;j<cylinders[i].nve;j++){
			double EVO = cylinders[i].exhaust_valves[j].angle_V0;
			double EVC = cylinders[i].exhaust_valves[j].angle_VC;
			if(modulo(theta_cyl-EVO,theta_cycle) >= 0. &&
			   modulo(theta_cyl-EVO,theta_cycle) <= modulo(EVC-EVO,theta_cycle)){
				nve++;
				int itube =	cylinders[i].exhaust_valves[j].tube;
				int nod_est = cylinders[i].nnod-cylinders[i].nve+j;
				for(unsigned int k=0;k<ndof;k++)
					Xn1[tubes[itube].i_new_state[k]] = 
						cylinders[i].new_state[nod_est*ndof+k];
			}
		}
		if(nve==cylinders[0].nve) break;
	}
}

/**
   Wrapper function that detect if the simulation is a engine or not, 
   and calls the corresponding function
*/
void Simulator::solver(){
	if (this->ncyl==0)
		this->solverNOEngine();
	else
		this->solverEngine();
}

/**
   Solves not engine simulation
*/
void Simulator::solverNOEngine(){
	cout<<"Not implemented yet"<<endl;
}
/**
   \brief Solves the engine Simulation
*/
void Simulator::solverEngine(){
	int show_info=100;
	for (irpm=0;irpm<nrpms;irpm++){
		createDir(true);
		openFortranUnits();
		time   = 0.0;
		lcycle = 1;
		icycle = 1;
		omega  = 2.*pi*rpms[irpm]/60.;
		iteration = 1;
		while(icycle<=ncycles){
			time += dt;
			theta = fmod(omega*time, theta_cycle);
			/** For the MRCVC engine, the chambers use the same
				intake and exhaust pipe, so we must to change the
				reference nodes for the corresponding pipes
			 **/
			if(engine_type==2) change_ref_state_tubes(theta);
			solveStep();
			// if(engine_type==2) correct_state_tubes(theta);
			actualizeState(); //actualizo al nuevo estado global
			actualizeDt();
			// icycle = floor((theta/nstroke)*pi)+1;
			icycle = floor(omega*time/theta_cycle)+1;
			if(!this->use_global_gas_prop && icycle!=lcycle){
				correct_gamma_exhaust(&(this->ga_exhaust));
				lcycle = icycle;
			}
			this->crank_angle = theta*180./pi;
			if(iteration%show_info==0)
				cout<<"cycle: "<<icycle<<" - crank angle: "
					<<crank_angle<<" deg"<<" - rpm: "<<rpms[irpm]<<endl;

			if(nappend>0){
				if(iteration%nappend==0){ // aca usar nappend
					saveHisto(iteration<=nappend);
				}
			}

			if(nsave>0){
				if(iteration%nsave==0){
					saveState();
				}
			}
			iteration++;
		}
		this->final_times.push_back(time);
		closeFortranUnits();
		createHeaderFile();	// this rpm was calculated. Refresh header file
		// compressFiles(); //compress files and clean the .txt
	}
	if(this->nsave!=0)		
		saveState();
}

/**
   \brief Solves one simulation step
*/
void Simulator::solveStep(){
	dataSim globalData;
	makeStruct(globalData);
	//cout<<"Pasa atmospheres"<<endl;
	for(int i=0;i<ntubes;i++){
		tubes[i].solver(globalData,Xn,Xn1,true);
	}
	//cout<<"Empieza solve step"<<endl;
	for(int i=0;i<natm;i++){
		atmospheres[i].solver(globalData,Xn,Xn1,false);
	}
	//cout<<"Pasa tubes"<<endl;
	for(int i=0;i<ncyl;i++){
		cylinders[i].solver(globalData,Xn,Xn1,false);
	}
	//cout<<"Pasa Cylinders"<<endl;
	for(int i=0;i<njunc;i++){
		junctions[i].solver(globalData,Xn,Xn1,false);	
	}
	//cout<<"Pasa Junctions"<<endl;
	for(int i=0;i<ntank;i++){
		tanks[i].solver(globalData,Xn,Xn1,false);	
	}
	//cout<<"Pasa tanks"<<endl;
}

/**
   \brief Actualizes the new global state vector
*/
void Simulator::actualizeState(){
	Xn = Xn1;
}

/**
   \brief Calculates the new time step
*/
void Simulator::actualizeDt(){
	dt = INT_MAX;
	for(int i=0;i<ntubes;i++){
		if(tubes[i].dt_max<dt)
			dt = tubes[i].dt_max;
	}
	//cout<<"paso de tiempo: "<<dt<<endl;
}

/**
   \brief Returns the time step
*/
double Simulator::GetTimeStep(){
	return dt;
}

/**
   \brief Sets a value for the time step
*/
void Simulator::SetTimeStep(double dT){
	dt = dT;
}

/**
   \brief Sets a value for time and crank angle
*/
void Simulator::SetTime(double t, int irpm){
	time  = t;
	omega = 2.*pi*rpms[irpm]/60.;
	theta = fmod(omega*time, theta_cycle);
}

/**
   \brief Returns the old state vector
*/
vector<double> Simulator::GetOldState(){
    return Xn;
}

/**
   \brief Returns the new state vector
*/
vector<double> Simulator::GetNewState(){
    return Xn1;
}

/**
   \brief Returns the length of old state vector
*/
int Simulator::GetOldStateSize(){
    return Xn.size();
}

/**
   \brief Returns the length of new state vector
*/
int Simulator::GetNewStateSize(){
    return Xn1.size();
}

/**
   \brief Sets values in the state vector
   \param i: position index in the array state
   \param val: value to be set in the array state
*/
void Simulator::SetStateValue(int i, double val){
    Xn[i] = val;
}

/**
   \brief Returns the vector of masses into the cylinder
*/
vector<double> Simulator::getCylinderMass(int icyl){
    return cylinders[icyl].getMass();
}

/**
   \brief Sets values in the cylinder mass vector
*/
void Simulator::setCylinderMass(int icyl, int i, double mass){
    cylinders[icyl].setMass(i, mass);
}

/**
   \brief Print the Global State in "printData.txt", is only for control
*/
void Simulator::printData(){
	ofstream archim;
	archim.open("printData.txt",ios::trunc);
    if(archim.is_open())
		{
			archim<<"tamano Xn: "<<Xn.size()<<endl;
			for(unsigned int k=0;k<Xn.size();k++){
				archim<<k<<":"<<Xn[k]<<", ";
			}
			archim<<endl<<endl<<"ATMOSPHERES:"<<endl;
			vector<Atmosphere>::iterator it_At = atmospheres.begin();
			while(it_At!=atmospheres.end()){
				vector<unsigned int>::iterator it2 = it_At->i_state.begin();
				while(it2!=it_At->i_state.end()){
					archim<<*it2<<", ";
					it2++;
				}
				archim<<" -- "<<"\n";
				it_At++;
			}
				
			archim<<endl<<endl<<"TUBOS:"<<endl;
			vector<Tube>::iterator it_T = tubes.begin();
			while(it_T!=tubes.end()){
				vector<unsigned int>::iterator it2 = it_T->i_state.begin();
				while(it2!=it_T->i_state.end()){
					archim<<*it2<<", ";
					it2++;
				}
				archim<<" -- "<<"\n";
				it_T++;
			}
			archim<<endl<<endl<<"JUNCTIONS:"<<endl;
			vector<Junction>::iterator it_J = junctions.begin();
			while(it_J!=junctions.end()){
				vector<unsigned int>::iterator it2 = it_J->i_state.begin();
				while(it2!=it_J->i_state.end()){
					archim<<*it2<<", ";
					it2++;
				}
				archim<<" -- "<<"\n";
				it_J++;
			}
			archim<<endl<<endl<<"CYLINDERS:"<<endl;
			vector<Cylinder>::iterator it_C = cylinders.begin();
			while(it_C!=cylinders.end()){
				vector<unsigned int>::iterator it2 = it_C->i_state.begin();
				while(it2!=it_C->i_state.end()){
					archim<<*it2<<", ";
					it2++;
				}
				archim<<" -- "<<"\n";
				it_C++;
			}
			archim<<endl<<endl<<"TANKS:"<<endl;
			vector<Tank>::iterator it_Ta = tanks.begin();
			while(it_Ta!=tanks.end()){
				vector<unsigned int>::iterator it2 = it_Ta->i_state.begin();
				while(it2!=it_Ta->i_state.end()){
					archim<<*it2<<", ";
					it2++;
				}
				archim<<" -- "<<"\n";
				it_Ta++;
			}
		}
	archim.close();
	cout<<"File printData.txt generated"<<endl;
}

/**
   \brief Makes the struct for send data to Fortran
*/
void Simulator::makeStruct(dataSim &data){
	data.time			= this->time;
	data.dt				= this->dt;
	data.dtheta_rpm		= this->dtheta_rpm;
	data.Courant		= this->Courant;
	data.ga				= this->ga;
	data.R_gas			= this->R_gas;
	data.theta			= this->theta;
	data.omega			= this->omega;
	data.iter_sim1d		= this->iter_sim1d;
	data.viscous_flow   = this->viscous_flow;
	data.heat_flow		= this->heat_flow;
	data.icycle			= this->icycle;
	data.rpm			= this->rpms[irpm];
	data.rpm_ini		= this->rpms[0];
	data.engine_type	= this->engine_type;
	data.theta_cycle    = this->theta_cycle;
	if(iteration%nappend==0)
		data.save_extras = true;
	else
		data.save_extras = false;
	data.ncyl	        = this->ncyl;
	data.use_global_gas_prop = (this->use_global_gas_prop ? true : false);
	data.ga_intake  = this->ga_intake;
	data.ga_exhaust = this->ga_exhaust;
}

/**
   Guarda el ultimo estado de Xn
*/
/*void Simulator::saveState(){
	ofstream archim;
	archim.open(filesave_state,ios::trunc);
	if(archim.is_open())
		{
			for(int k=0;k<natm;k++){
				for(unsigned int i=0;i<atmospheres[k].nnod;i++){
					string aux = "";
					for(unsigned int j=0;j<atmospheres[k].ndof;j++){
						double value = Xn[atmospheres[k].i_state[i*atmospheres[k].ndof+j]];
						stringstream ss;
						ss.precision(10);
						ss.width(20);
						ss<<value;
						aux += ss.str();
					}
					archim<<aux<<"\n";
				}
			}
			
			for(int k=0;k<ntubes;k++){
				for(unsigned int i=0;i<tubes[k].nnod;i++){
					string aux = "";
					for(unsigned int j=0;j<tubes[k].ndof;j++){
						double value = Xn[tubes[k].i_state[i*tubes[k].ndof+j]];
						stringstream ss;
						ss.precision(10);
						ss.width(20);
						ss<<value;
						aux += ss.str();
					}
					archim<<aux<<"\n";
				}
			}
			for(int k=0;k<ncyl;k++){
				for(unsigned int i=0;i<cylinders[k].nnod;i++){
					string aux = "";
					for(unsigned int j=0;j<cylinders[k].ndof;j++){
						double value = Xn[cylinders[k].i_state[i*cylinders[k].ndof+j]];
						stringstream ss;
						ss.precision(10);
						ss.width(20);
						ss<<value;
						aux += ss.str();
					}
					archim<<aux<<"\n";
				}
			}
			for(int k=0;k<njunc;k++){
				for(unsigned int i=0;i<junctions[k].nnod;i++){
					string aux = "";
					for(unsigned int j=0;j<junctions[k].ndof;j++){
						double value = Xn[junctions[k].i_state[i*junctions[k].ndof+j]];
						stringstream ss;
						ss.precision(10);
						ss.width(20);
						ss<<value;
						aux += ss.str();
					}
					archim<<aux<<"\n";
				}
			}
			for(int k=0;k<ntank;k++){
				for(unsigned int i=0;i<tanks[k].nnod;i++){
					string aux = "";
					for(unsigned int j=0;j<tanks[k].ndof;j++){
						double value = Xn[tanks[k].i_state[i*tanks[k].ndof+j]];
						stringstream ss;
						ss.precision(10);
						ss.width(20);
						ss<<value;
						aux += ss.str();
					}
					archim<<aux<<"\n";
				}
			}
			
			archim.close();	
			
		}else{
		cout<<"No se pudo abrir el archivo para guardar"<<endl;
	}
}
*/

/**
   \brief Read the state from binary file, and assign it to Global State
*/
void Simulator::readState(){
	int l;
	FILE* archim;
	archim = fopen(filein_state,"rb");
	if(archim)
		{
			fseek(archim,0,SEEK_END);
  			l = ftell(archim);
			fseek(archim,0,SEEK_SET);
			l = l/sizeof(double);
			cout<<"L: "<<l<<endl;
			Xn.resize(l);			
			fread(&Xn[0],sizeof(double),l,archim);
			fclose(archim);	
		}else{
		cout<<"File "<<filein_state<<" can't be opened"<<endl;
	}
}

/**
   \brief Save the state to binary file
*/
void Simulator::saveState(){
	char* file = strconcat(this->folderRPM,(char *)"/");
	file = strconcat(file,filesave_state);
	FILE* archim;
	archim = fopen(file,"wb");
	if(archim)
		{
			int l = Xn.size();
			double* value = &Xn[0];
			fwrite(value,sizeof(double),l,archim);
			fclose(archim);	
		}else{
		cout<<"File "<<file<<" can't be opened"<<endl;
	}
	free(file);
}

/*
   \brief Checks if a directory exists
*/
int dirExists(const char *path)
{
    struct stat info;

    if(stat( path, &info ) != 0)
        return 0;
    else if(info.st_mode & S_IFDIR)
        return 1;
    else
        return 0;
}

/**
   \brief Create folder for save the data for the actual RPM
*/
void Simulator::createDir(bool newRPM){
	if(!newRPM){
#ifdef __linux__
		char mk[] = "mkdir -p ";
		char runsChar[] = "runs/";
#endif
#ifdef _WIN32
		char mk[] = "mkdir ";
		char runsChar[] = "runs\\";
#endif
		char* folder = strconcat(runsChar,folder_name);
		char* makeFolder = strconcat(mk,folder);
		if (!dirExists(folder)) system(makeFolder);
		strcopy(this->folderGral,folder);
	}
	else{
#ifdef __linux__
		char mk[] = "mkdir -p ";
		char* folder = strconcat(this->folderGral,(char*)"/RPM_");
#endif
#ifdef _WIN32
		char mk[] = "mkdir ";
		char* folder = strconcat(this->folderGral,(char*)"\\RPM_");
#endif
		char* out = int2char(rpms[irpm]);
		folder = strconcat(folder,out);
		char* makeFolderRPM = strconcat(mk,folder);		
		if (!dirExists(folder)) system(makeFolderRPM);
		strcopy(this->folderRPM,folder);
		cout<<"Folder created: "<<this->folderRPM<<endl;
		free(out);
	}
}

/**
   \brief Open Units files in Fortran for save extra's histo
*/
void Simulator::openFortranUnits(){
	int nu = 8; //empiezo desde la unidad 8	
	for(int i=0;i<ncyl;i++){
		if(this->cylinders[i].extras){
			this->cylinders[i].nunit = nu;
			char* indx = int2char(i);
			char* file = strconcat(this->folderRPM,(char*)"/cyl_extras_");
			file = strconcat(file,indx);
			file = strconcat(file,(char*)".txt");
			this->cylinders[i].openFortranUnit(file);
			nu++;
		}
	}
	for(int i=0;i<ntank;i++){
		if(this->tanks[i].extras){
			this->tanks[i].nunit = nu;
			char* indx = int2char(i);
			char* file = strconcat(this->folderRPM,(char*)"/tank_extras_");
			file = strconcat(file,indx);
			file = strconcat(file,(char*)".txt");
			this->tanks[i].openFortranUnit(file);
			nu++;
		}
	}
}

/**
   \brief Close the File Units opened for save extra's histo
*/
void Simulator::closeFortranUnits(){
	for(int i=0;i<ncyl;i++){
		if(this->cylinders[i].extras){
			this->cylinders[i].closeFortranUnit();
		}
	}
	for(int i=0;i<ntank;i++){
		if(this->tanks[i].extras){
			this->tanks[i].closeFortranUnit();
		}
	}
}

/**
   \brief Save the histo for all components
   \param first: Indicates if open new (true) or append (false) a file
*/
void Simulator::saveHisto(bool first){
	vector<double>aux;
	for(int k=0;k<ntubes;k++){
		char* indx = int2char(k);
		char* file = strconcat(folderRPM,(char*)"/tube_");
		file = strconcat(file,indx);
		file = strconcat(file,(char*)".txt");
		tubes[k].saveHisto(first,file,icycle,crank_angle,time,tubes[k].xnod);
	}
	for(int k=0;k<ncyl;k++){
		char* indx = int2char(k);
		char* file = strconcat(folderRPM,(char*)"/cyl_");
		file = strconcat(file,indx);
		file = strconcat(file,(char*)".txt");
		cylinders[k].saveHisto(first,file,icycle,crank_angle,time,aux);
	}
	for(int k=0;k<ntank;k++){
		char* indx = int2char(k);
		char* file = strconcat(folderRPM,(char*)"/tank_");
		file = strconcat(file,indx);
		file = strconcat(file,(char*)".txt");
		tanks[k].saveHisto(first,file,icycle,crank_angle,time,aux);
	}
	for(int k=0;k<njunc;k++){
		char* indx = int2char(k);
		char* file = strconcat(folderRPM,(char*)"/junc_");
		file = strconcat(file,indx);
		file = strconcat(file,(char*)".txt");
		junctions[k].saveHisto(first,file,icycle,crank_angle,time,aux);
	}
}

/**
   \brief Compress files to .bz2 and remove *.txt
*/
void Simulator::compressFiles(){
	for(int k=0;k<ntubes;k++){
		char* indx = int2char(k);
		char* file = strconcat(folderRPM,(char*)"/tube_");
		file = strconcat(file,indx);
		file = strconcat(file,(char*)".txt");
		char* sys = strconcat((char*) "tar -jcvf ",file);
		sys = strconcat(sys,(char*)".tar.bz2 ");
		sys = strconcat(sys,file);
		system(sys);
		char* rm =  strconcat((char*) "rm ",file);
		system(rm);
	}
	for(int k=0;k<ncyl;k++){
		char* indx = int2char(k);
		char* file = strconcat(folderRPM,(char*)"/cyl_");
		file = strconcat(file,indx);
		file = strconcat(file,(char*)".txt");
		char* sys = strconcat((char*) "tar -jcvf ",file);
		sys = strconcat(sys,(char*)".tar.bz2 ");
		sys = strconcat(sys,file);
		system(sys);
		char* rm =  strconcat((char*) "rm ",file);
		system(rm);
		if(this->cylinders[k].extras){
			char* file2 = strconcat(folderRPM,(char*)"/cyl_extras_");
			file2 = strconcat(file2,indx);
			file2 = strconcat(file2,(char*)".txt");
			char* sys2 = strconcat((char*) "tar -jcvf ",file2);
			sys2 = strconcat(sys2,(char*)".tar.bz2 ");
			sys2 = strconcat(sys2,file2);
			system(sys2);
			char* rm2 =  strconcat((char*) "rm ",file2);
			system(rm2);
		}
	}
	for(int k=0;k<ntank;k++){
		char* indx = int2char(k);
		char* file = strconcat(folderRPM,(char*)"/tank_");
		file = strconcat(file,indx);
		file = strconcat(file,(char*)".txt");
		char* sys = strconcat((char*) "tar -jcvf ",file);
		sys = strconcat(sys,(char*)".tar.bz2 ");
		sys = strconcat(sys,file);
		system(sys);
		char* rm =  strconcat((char*) "rm ",file);
		system(rm);
		if(this->tanks[k].extras){
			char* file2 = strconcat(folderRPM,(char*)"/tank_extras_");
			file2 = strconcat(file2,indx);
			file2 = strconcat(file2,(char*)".txt");
			char* sys2 = strconcat((char*) "tar -jcvf ",file2);
			sys2 = strconcat(sys2,(char*)".tar.bz2 ");
			sys2 = strconcat(sys2,file2);
			system(sys2);
			char* rm2 =  strconcat((char*) "rm ",file);
			system(rm2);		
		}
	}
	for(int k=0;k<njunc;k++){
		char* indx = int2char(k);
		char* file = strconcat(folderRPM,(char*)"/junc_");
		file = strconcat(file,indx);
		file = strconcat(file,(char*)".txt");
		char* sys = strconcat((char*) "tar -jcvf ",file);
		sys = strconcat(sys,(char*)".tar.bz2 ");
		sys = strconcat(sys,file);
		system(sys);
		char* rm =  strconcat((char*) "rm ",file);
		system(rm);
	}
}

/**
   \brief Generate one header file for rpm (replace the lastest). Support a stop in run.
*/
void Simulator::createHeaderFile(){
	char* file = strconcat(this->folderGral,(char *)"/header.py");
	ofstream archim;
	archim.open(file,ios::trunc);
	
	if(archim.is_open()){
		archim<<"rpms = [";
		for(int i=0;i<irpm+1;i++){
			if(i<irpm)			
				archim<<rpms[i]<<", ";
			else
				archim<<rpms[i]<<"]"<<endl<<endl;
		}
		archim<<"final_times = [";
		
		int ft = this->final_times.size();
		for(int i=0;i<ft;i++){
			if((i+1)<ft)			
				archim<<this->final_times[i]<<", ";
			else
				archim<<this->final_times[i]<<"]"<<endl<<endl;
		}
		archim<<"nstroke = "<<theta_cycle/pi<<endl;
		archim<<"ncycles = "<<ncycles<<endl;
		archim<<"rho = "<<Xn[0]<<endl;
		archim<<"Globals = dict()"<<endl;
		archim<<"Globals['engine_data'] = "<<int(this->calc_engine_data)<<endl;
		
		archim<<"Tubes = []"<<endl;
		for(int i=0;i<ntubes;i++){
			archim<<"Tube"<<i<<" = dict()"<<endl;
			archim<<"Tube"<<i<<"['label'] = '"<<tubes[i].label<<"'"<<endl;
			archim<<"Tube"<<i<<"['nnod'] = "<<tubes[i].nnod<<endl;
			archim<<"Tube"<<i<<"['ndof'] = "<<tubes[i].ndof<<endl;
			archim<<"Tube"<<i<<"['histo'] = [";
			int l = tubes[i].histo.size();
			for(int j=0;j<l;j++){
				if(j+1<l)				
					archim<<tubes[i].histo[j]<<", ";
				else
					archim<<tubes[i].histo[j];
			}		
			archim<<"]"<<endl;
			archim<<"Tubes.append(Tube"<<i<<")"<<endl<<endl;
		}

		archim<<"Tanks = []"<<endl;
		for(int i=0;i<ntank;i++){
			archim<<"Tank"<<i<<" = dict()"<<endl;
			archim<<"Tank"<<i<<"['label'] = '"<<tanks[i].label<<"'"<<endl;
			archim<<"Tank"<<i<<"['nnod'] = "<<tanks[i].nnod<<endl;
			archim<<"Tank"<<i<<"['ndof'] = "<<tanks[i].ndof<<endl;
			archim<<"Tank"<<i<<"['extras'] = "<<int(tanks[i].extras)<<endl;
			archim<<"Tank"<<i<<"['histo'] = [";
			int l = tanks[i].histo.size();
			for(int j=0;j<l;j++){
				if(j+1<l)				
					archim<<tanks[i].histo[j]<<", ";
				else
					archim<<tanks[i].histo[j];
			}		
			archim<<"]"<<endl;
			archim<<"Tanks.append(Tank"<<i<<")"<<endl<<endl;
		}

		archim<<"Junctions = []"<<endl;
		for(int i=0;i<njunc;i++){
			archim<<"Junction"<<i<<" = dict()"<<endl;
			archim<<"Junction"<<i<<"['label'] = '"<<junctions[i].label<<"'"<<endl;
			archim<<"Junction"<<i<<"['nnod'] = "<<junctions[i].nnod<<endl;
			archim<<"Junction"<<i<<"['ndof'] = "<<junctions[i].ndof<<endl;
			archim<<"Junction"<<i<<"['histo'] = [";
			int l = junctions[i].histo.size();
			for(int j=0;j<l;j++){
				if(j+1<l)				
					archim<<junctions[i].histo[j]<<", ";
				else
					archim<<junctions[i].histo[j];
			}		
			archim<<"]"<<endl;
			archim<<"Junctions.append(Junction"<<i<<")"<<endl<<endl;
		}

		archim<<"Cylinders = []"<<endl;
		
		for(int i=0;i<ncyl;i++){
			archim<<"Cylinder"<<i<<" = dict()"<<endl;
			archim<<"Cylinder"<<i<<"['label'] = '"<<cylinders[i].label<<"'"<<endl;
			archim<<"Cylinder"<<i<<"['ndof'] = "<<cylinders[i].ndof<<endl;
			archim<<"Cylinder"<<i<<"['nvi'] = "<<cylinders[i].nvi<<endl;
			archim<<"Cylinder"<<i<<"['nve'] = "<<cylinders[i].nve<<endl;
			archim<<"Cylinder"<<i<<"['extras'] = "<<int(cylinders[i].extras)<<endl;
			archim<<"Cylinder"<<i<<"['Q_fuel'] = "<<cylinders[i].fuel_data.Q_fuel<<endl;
			archim<<"Cylinder"<<i<<"['crank_radius'] = "<<cylinders[i].crank_radius<<endl;
			archim<<"Cylinder"<<i<<"['histo'] = [";
			int l = cylinders[i].histo.size();
			for(int j=0;j<l;j++){
				if(j+1<l)				
					archim<<cylinders[i].histo[j]<<", ";
				else
					archim<<cylinders[i].histo[j];
			}	
			archim<<"]"<<endl;
			// determino el angulo en donde el cylinder esta completamente cerrado
			double angleClose = 0;
			int li = cylinders[i].intake_valves.size();
			int le = cylinders[i].exhaust_valves.size();
			for(int j=0;j<li;j++){
				if(cylinders[i].intake_valves[j].angle_VC > angleClose)
					angleClose = cylinders[i].intake_valves[j].angle_VC;
			}
			for(int j=0;j<le;j++){
				if(cylinders[i].exhaust_valves[j].angle_VC > angleClose)
					angleClose = cylinders[i].exhaust_valves[j].angle_VC;
			}	
			archim<<"Cylinder"<<i<<"['angleClose'] = "<<angleClose*180/pi<<endl;
			archim<<"Cylinders.append(Cylinder"<<i<<")"<<endl<<endl;	
		}
		archim.close();
	}
}
