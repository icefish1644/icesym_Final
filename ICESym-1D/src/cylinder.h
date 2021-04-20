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

#ifndef _CYLINDER_H_
#define _CYLINDER_H_
#include "component.h"

using namespace std;

/**
   Defines the datatype "Fuel"
*/
typedef struct
{
	double Q_fuel;    /**< Lower Heating Value of fuel (Poder calorífico 
						 inferior del combustible) */
	double y;         /**< H/C ratio of fuel (Relationship between the number of
							H and C atoms in the fuel molecule)  */
	double alpha;     /**< Number of C atoms in the fuel molecule */
	double beta;      /**< Number of H atoms in the fuel molecule */
	double gamma;     /**< Number of O atoms in the fuel molecule */
	double delta;     /**< Number of N atoms in the fuel molecule */
	double Mw;        /**< Molecular weight of fuel */
	double hvap_fuel; /**< Vaporization Heat of fuel (Calor de vaporización 
						 del combustible)   */
	vector<double> coef_cp; /**< Coefficients for the computation of the 
							   fuel's cp */
}fuel;

/**
   Defines the datatype "Valve"
*/
typedef struct
{
	int Nval;				/**< Number of Valves (Número de válvulas) */
	int type_dat;			/**< Identifies how input Lv 0:"Exponential", 1:"Sin²", 2:"user-defined" (Identifica cómo se ingresa la alzada: mediante una ley predefinida o mediante un archivo) */
	vector<double> Cd;		/**< Discharge Coefficient */
	vector<double> Lv;		/**< Arrangement containing valve lift  */
	double* dx_tube;	    /**< Size of tube's element connected */
	double* Area_tube;	    /**< Area of tube's element connected */
	double* twall_tube;	    /**< Temperature of tube's element connected (Temperatura del nodo del tubo conectado) */
	double* dAreax_tube;	/**< Area differential of tube's element connected (derivada del area del nodo del tubo conectado) */
	double angle_V0;		/**< Valve's Angle opening (Angulo de apertura de la válvula) */
	double angle_VC;		/**< Valve's Angle closing (Angulo de cierre de la válvula) */
	double Dv;				/**< Valve's diameter (Diámetro de la válvula) */
	double Lvmax;			/**< Valve's maximum Lv (Alzada máxima de la válvula) */
	int valve_model;		/**< Valve Model 0:"Toyota", 1:"Alessandri"*/
	int tube;				/**< Tube's index connected to Valve */
}valve;

/**
   Defines datatype "Injection"
*/
typedef struct
{
	int pulse;          			/**< Identifies law type of fuel injection (Identifica el tipo de ley con que se inyecta el combustible) */
	double m_inj;					/**< Fuel mass injected for cycle */
	double dtheta_inj;				/**< Injection duration, measure in crank angle */
	double T_fuel;					/**< Temperature of fuel injection */
	double theta_inj_ini; 			/**< Angle of start the injection  */
	double theta_id;				/**< Angle delay of ignition (can be data or calculated internally) */
	int ignition_delay_model;		/**< Ignition delay Model 0:"L-W", 1:"H-H", 2:"user-defined"*/
	double integral;				/**< Variable used to integrate the ratio t / t_d over time  */
	vector<double> mfdot_array; 	/**< Injected Mass of fuel in angle's function (Array containing the fuel injected mass as a function of the angle) */
}injection;

/**
   Defines datatype "Combustion"
*/
typedef struct
{
	double theta_ig_0;				/**< Start angle of combustion */
	double dtheta_comb;				/**< Angle differential of combustion */
	double phi;						/**< Equivalence relationship [(a/f)/(a/f)steq] (Relación de equivalencia) */
	double phi_ig;					/**< Equivalence relationship at start combustion */
	double a_wiebe;					/**< Combustion Efficiency Parameter */
	double m_wiebe;					/**< Shape Parameter */
	int combustion_model;			/**< Combustion Model  0: "user-defined", 1: "Wiebe-2" (default), 2: "Wiebe-3", 3: "Watson" , 4: "<none>"*/
	bool start_comb;				/**< Indicates if the combustion start or not */
	vector<double> xbdot_array; 	/**< Burned Mass Fraction rate */
}combustion; 

/**
   Defines datatype "Scavenge"
*/
typedef struct
{
	double val_1;
	double val_2;
	double SRv;
	bool close_cyl;
}Scavenge;

/**
  	Cylinder Class
*/
class Cylinder: public Component 
{
 public:
	Cylinder(unsigned int, unsigned int, unsigned int, int, vector<double>, vector<int>, 
			 char*, double, double, double, double, double, double,
	         double, double, vector<double>, vector<double>, vector<double>, 
			 vector<double>,vector<double>, int, double, int, int, int, int, fuel, 
			 combustion, injection,vector<valve>, vector<valve>, Scavenge, int,int,
			 int, double, double, double);
	Cylinder(Cylinder* c);
	Cylinder(){};
	void makeStruct(dataCylinder &data);
	void undoStruct(dataCylinder &data);
	void initFortran(int icyl,dataSim &globalData);
	void calculate_state(double* atm,dataSim &globalData);
	void openFortranUnit(char* file);
	void closeFortranUnit();
	
	vector<valve> intake_valves;
	vector<valve> exhaust_valves;
	unsigned int nvi;					/**< Number of Intake Valves */	
	unsigned int nve;					/**< Number of Exhaust Valves */
	bool extras;				  		/**< Flag to Save internal variables in fortran units */	
	int nunit;							/**< Number of fortran unit file */
	fuel fuel_data; 	
	double crank_radius;      /**< Crank's diameter */

	vector<double> getMass();
	void setMass(int, double);

	double theta_0;           /**< Piston's Initial position angle */
 protected:
	
 private:
	double Bore;              /**< Cylinder's diameter*/
	double Vol_clearance;     /**< Combustion's chamber's Volume */
	double rod_length;		  /**< Rod's Length */
	double head_chamber_area; /**< Combustion's chamber's Head Area (Surface area of the chamber) */
	double piston_area;       /**< Piston's Head area = pi/4 * Bore^2 */
	double delta_ca;          /**< Angle between crankshafts (only for opposed pistons) */
	vector<double> Twall;     /**< Cylinder's Wall Temperature (size=1: homogeneus, size=4: piston, intake, exhaust, liners) */
	vector<double> prop; 
	vector<double> U_crevice;
	vector<double> data_crevice;
	vector<double> mass_C;    /**< array of Masses inside Cylinder */
	int model_ht;             /**< Heat transfer model (0:"Annand", 1:"Woschni 1", 2:"Woschni 2", 3:"Taylor") */
	double factor_ht;	      /**< Multiplicative factor applied to heat transfer law */
	bool scavenge;			  /**< Indicates if will be used scavenge */
	int scavenge_type;	  /**< Scavenge type ("uniflow", "scre", "yam1", "yam6", "cd", "qubcr") */
	int type_ig;			  /**< Ignition type 0:gasoline (SI Engine), 1: Diesel (CI Engine) */
	bool full_implicit;
	Scavenge scavenge_data;		
	injection injection_data;
	combustion combustion_data;
	int icyl;				  /**< Index of this cylinder in global array*/
	int species_model;		  /**< Type of Species Model 0:none, 1:single-component */
	
	void calculate(dataSim &globalData);

	/**
	   Definitions of geometrical parameters for the MRCVC engine
	 **/
	int nvanes;           /**< Number of vanes (n) */
	double major_radius;  /**< Radius of the vanes's center (R) */
	double minor_radius;  /**< Radius of the vanes (r) */
	double chamber_heigh; /**< Heigh of the chamber (h) */
};

extern "C"{
	void initialize_arrays(int* icyl, double* prop,double* U_crevice, double* data_crevice, 
						   int*l1, int*l2, int*l3);
	void initialize_valves(int* icyl, int* nvi, int* nve);
	void initialize_fuel(int* icyl, fuel* fuelData);
	void initialize_scavenge(int* icyl, Scavenge* scavengeData);
	void initialize_injection(int* icyl, int* pulse, double* m_inj, double* dtheta_inj, 
							  double* T_fuel, double* theta_inj_ini, double* theta_id, double* integral, 
							  double* mfdot_array, int* ignition_delay_model, int* l1);
	void initialize_combustion(int* icyl, double* theta_ig_0, double* dtheta_comb, double* phi, 
							   double* phi_ig, double* a_wiebe, double* m_wiebe, double* xbdot_array, 
							   int* combustion_model, bool* start_comb, int* l1);
	void initialize_exhaust_valves(int* icyl, int* ival, int* Nval, int* type_dat, double* angle_V0,
								   double* angle_VC, double* Dv, double* Lvmax, double* Cd, double* Lv,
								   int* valve_model, int* l1, int* l2, double* dx_tube, double* Area_tube, 
								   double* twall_tube, double* dAreax_tube, int* tube, double* theta_0,
								   dataSim* globalData);
	void initialize_intake_valves(int* icyl, int* ival, int* Nval, int* type_dat, double* angle_V0,
								  double* angle_VC, double* Dv, double* Lvmax, double* Cd, double* Lv,
								  int* valve_model, int* l1, int* l2, double* dx_tube, double* Area_tube, 
								  double* twall_tube, double* dAreax_tube, int* tube, double* theta_0,
								  dataSim* globalData);
	void open_unit(int* nu, char* file, int* nfsize);
	void close_unit(int* nu);
}
#endif //  _CYLINDER_H_
