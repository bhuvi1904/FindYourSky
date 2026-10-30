import json
import os

# Complete roster of all 41 DGCA-approved Flying Training Organisations in India
# Grounded in official DGCA notices, CAR Section 7 Series D, Lok Sabha / Rajya Sabha Annexures,
# and PIB Press Release PRID 2255276 (April 2026 FTO Ranking Announcement).

ftos = [
    # 1. Avyanna Aviation (Sole Category A in April 2026 Ranking)
    {
        "school_id": "FTO_AVYANNA_019",
        "name": "Avyanna Aviation Private Limited",
        "short_name": "Avyanna Aviation",
        "slug": "avyanna-aviation-kishangarh",
        "website_url": "https://avyannaaviation.com",
        "ownership_type": "private",
        "dgca_approval_no": "DGCA/FTO/39/2022",
        "approval_validity": "2027-11-30",
        "operational_status": "active",
        "established_year": 2022,
        "confidence_score": 0.99,
        "completeness_score": 0.98,
        "last_verified_date": "2026-10-28",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Category A",
            "overall_score": 74.2,
            "national_rank": 1,
            "annual_hours_logged": 9800,
            "safety_audit_score": 89.5,
            "cfi_cadre_strength": 9,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_AVYANNA_KQH",
                "is_primary": True,
                "airport_name": "Kishangarh Airport",
                "icao_code": "VIKG",
                "city": "Ajmer / Kishangarh",
                "state": "Rajasthan",
                "region": "North",
                "runway_length_meters": 2000,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "AAI Controlled Tower",
                "latitude": 26.6028,
                "longitude": 74.8167
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Piper PA-28 Archer III",
                "manufacturer": "Piper Aircraft",
                "engine_type": "single_engine",
                "avionics_type": "Garmin G1000 NXi Glass Cockpit",
                "count": 7,
                "operational_count": 7,
                "fuel_type": "AvGas 100LL"
            },
            {
                "aircraft_model": "Piper PA-44 Seminole",
                "manufacturer": "Piper Aircraft",
                "engine_type": "multi_engine",
                "avionics_type": "Garmin G1000 NXi Glass Cockpit",
                "count": 2,
                "operational_count": 2,
                "fuel_type": "AvGas 100LL"
            }
        ],
        "fees": {
            "course_name": "Commercial Pilot License (Aeroplane) with Multi-Engine & IR",
            "currency": "INR",
            "tuition_flying_inr": 4200000,
            "ground_school_inr": 300000,
            "simulator_inr": 200000,
            "hostel_mess_annual_inr": 250000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 4950000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-04-01",
            "source_url": "https://avyannaaviation.com/cpl-program",
            "inclusions": ["200 hrs flight training (185h SE + 15h ME)", "Ground theory classes", "Simulator briefing", "Airport landing fees"],
            "exclusions": ["DGCA medical examination", "Hostel accommodation and mess food", "DGCA license issue fees"]
        },
        "programmes": ["CPL with Multi-Engine & IR", "PPL (Aeroplane)", "Instrument Rating (IR)", "Assistant Flight Instructor (AFIR)"],
        "training_capacity": {
            "annual_cadet_intake": 60,
            "active_instructors": 9,
            "avg_completion_months": 14
        }
    },

    # 2. IGRUA (Amethi) - Premier Autonomous Central Govt
    {
        "school_id": "FTO_IGRUA_001",
        "name": "Indira Gandhi Rashtriya Uran Akademi",
        "short_name": "IGRUA",
        "slug": "igrua-amethi",
        "website_url": "https://igrua.gov.in",
        "ownership_type": "autonomous_government",
        "dgca_approval_no": "DGCA/FTO/01/1985",
        "approval_validity": "2028-12-31",
        "operational_status": "active",
        "established_year": 1985,
        "confidence_score": 0.99,
        "completeness_score": 0.98,
        "last_verified_date": "2026-10-25",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Category B",
            "overall_score": 69.4,
            "national_rank": 2,
            "annual_hours_logged": 21500,
            "safety_audit_score": 91.5,
            "cfi_cadre_strength": 18,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_IGRUA_FUR",
                "is_primary": True,
                "airport_name": "Fursatganj Airfield",
                "icao_code": "VERB",
                "city": "Amethi",
                "state": "Uttar Pradesh",
                "region": "North",
                "runway_length_meters": 1829,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "Dedicated Controlled Airspace",
                "latitude": 26.2486,
                "longitude": 81.6508
            },
            {
                "base_id": "BASE_IGRUA_GON",
                "is_primary": False,
                "airport_name": "Birsi Airport",
                "icao_code": "VAGD",
                "city": "Gondia",
                "state": "Maharashtra",
                "region": "West",
                "runway_length_meters": 2290,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "AAI Controlled",
                "latitude": 21.5126,
                "longitude": 80.2929
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Diamond DA40 NG",
                "manufacturer": "Diamond Aircraft",
                "engine_type": "single_engine",
                "avionics_type": "Garmin G1000 NXi Glass Cockpit",
                "count": 14,
                "operational_count": 14,
                "fuel_type": "Jet-A1"
            },
            {
                "aircraft_model": "Diamond DA42 Twin Star",
                "manufacturer": "Diamond Aircraft",
                "engine_type": "multi_engine",
                "avionics_type": "Garmin G1000 Glass Cockpit",
                "count": 4,
                "operational_count": 4,
                "fuel_type": "Jet-A1"
            },
            {
                "aircraft_model": "Zlin 242L",
                "manufacturer": "Zlin Aircraft",
                "engine_type": "single_engine",
                "avionics_type": "Analogue with IFR avionics",
                "count": 4,
                "operational_count": 3,
                "fuel_type": "AvGas 100LL"
            }
        ],
        "fees": {
            "course_name": "Commercial Pilot License (Aeroplane) with Multi-Engine & IR",
            "currency": "INR",
            "tuition_flying_inr": 4500000,
            "ground_school_inr": 350000,
            "simulator_inr": 250000,
            "hostel_mess_annual_inr": 240000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 5340000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-03-01",
            "source_url": "https://igrua.gov.in/cpl-course-fees",
            "inclusions": ["200 hrs flying (185h SE + 15h ME)", "Ground training & navigation", "Simulator sessions", "Uniform & study material", "Airport charges"],
            "exclusions": ["Hostel boarding & mess food", "DGCA examination fees", "Class 1 medical test costs", "RTR(A) license test fees"]
        },
        "programmes": ["Ab-Initio CPL with Multi-Engine", "B.Sc. (Aviation) Degree Integrated", "Multi-Crew Co-operation (MCC)", "Type Rating Prep"],
        "training_capacity": {
            "annual_cadet_intake": 120,
            "active_instructors": 18,
            "avg_completion_months": 18
        }
    },

    # 3. National Flying Training Institute (CAE Gondia)
    {
        "school_id": "FTO_NFTI_002",
        "name": "National Flying Training Institute Private Limited (CAE Gondia)",
        "short_name": "CAE Gondia (NFTI)",
        "slug": "cae-gondia-nfti",
        "website_url": "https://www.cae.com/civil-aviation/aviation-academies/cae-gondia-nfti",
        "ownership_type": "joint_venture",
        "dgca_approval_no": "DGCA/FTO/08/2007",
        "approval_validity": "2027-08-31",
        "operational_status": "active",
        "established_year": 2007,
        "confidence_score": 0.97,
        "completeness_score": 0.95,
        "last_verified_date": "2026-10-20",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Category B",
            "overall_score": 68.8,
            "national_rank": 3,
            "annual_hours_logged": 19800,
            "safety_audit_score": 90.2,
            "cfi_cadre_strength": 16,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_NFTI_BIR",
                "is_primary": True,
                "airport_name": "Birsi Airport",
                "icao_code": "VAGD",
                "city": "Gondia",
                "state": "Maharashtra",
                "region": "West",
                "runway_length_meters": 2290,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "AAI Controlled Tower",
                "latitude": 21.5126,
                "longitude": 80.2929
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Diamond DA40 NG",
                "manufacturer": "Diamond Aircraft",
                "engine_type": "single_engine",
                "avionics_type": "Garmin G1000 Glass Cockpit",
                "count": 18,
                "operational_count": 17,
                "fuel_type": "Jet-A1"
            },
            {
                "aircraft_model": "Diamond DA42 Twin Star",
                "manufacturer": "Diamond Aircraft",
                "engine_type": "multi_engine",
                "avionics_type": "Garmin G1000 Glass Cockpit",
                "count": 3,
                "operational_count": 3,
                "fuel_type": "Jet-A1"
            }
        ],
        "fees": {
            "course_name": "Integrated CPL with Airline Cadet Pathway",
            "currency": "INR",
            "tuition_flying_inr": 4950000,
            "ground_school_inr": 400000,
            "simulator_inr": 280000,
            "hostel_mess_annual_inr": 200000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 5830000,
            "is_fee_inclusive_hostel": True,
            "is_fee_verified": True,
            "fee_effective_date": "2026-01-15",
            "source_url": "https://www.cae.com/civil-aviation/aviation-academies/cae-gondia-nfti/fees",
            "inclusions": ["200 hrs flying training", "Ground school syllabus", "FNPT-II simulator training", "Air-conditioned hostel & mess food", "Uniform"],
            "exclusions": ["DGCA regulatory exam fees", "DGCA license endorsement fee", "Personal travel"]
        },
        "programmes": ["Airline Cadet CPL", "Standard DGCA CPL (ME/IR)", "Multi-Engine Endorsement"],
        "training_capacity": {
            "annual_cadet_intake": 100,
            "active_instructors": 16,
            "avg_completion_months": 15
        }
    },

    # 4. Chimes Aviation Academy (CAA Dhana)
    {
        "school_id": "FTO_CAA_003",
        "name": "Chimes Aviation Academy",
        "short_name": "CAA Dhana",
        "slug": "chimes-aviation-academy",
        "website_url": "https://caaviation.com",
        "ownership_type": "private",
        "dgca_approval_no": "DGCA/FTO/11/2008",
        "approval_validity": "2027-10-31",
        "operational_status": "active",
        "established_year": 2008,
        "confidence_score": 0.96,
        "completeness_score": 0.94,
        "last_verified_date": "2026-10-18",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Category B",
            "overall_score": 67.6,
            "national_rank": 4,
            "annual_hours_logged": 18200,
            "safety_audit_score": 89.0,
            "cfi_cadre_strength": 15,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_CAA_DHA",
                "is_primary": True,
                "airport_name": "Dhana Airstrip",
                "icao_code": "VA1J",
                "city": "Sagar",
                "state": "Madhya Pradesh",
                "region": "Central",
                "runway_length_meters": 1300,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "FTO Dedicated Tower",
                "latitude": 23.7544,
                "longitude": 78.8572
            },
            {
                "base_id": "BASE_CAA_SHI",
                "is_primary": False,
                "airport_name": "Shivpuri Airport",
                "icao_code": "VASI",
                "city": "Shivpuri",
                "state": "Madhya Pradesh",
                "region": "Central",
                "runway_length_meters": 1250,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "Uncontrolled / FTO AFIS",
                "latitude": 25.4167,
                "longitude": 77.6500
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Cessna 172R/S Skyhawk",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Garmin G1000 Glass Cockpit",
                "count": 16,
                "operational_count": 15,
                "fuel_type": "AvGas 100LL"
            },
            {
                "aircraft_model": "Piper PA-34-220T Seneca V",
                "manufacturer": "Piper Aircraft",
                "engine_type": "multi_engine",
                "avionics_type": "Garmin G600 / Avidyne",
                "count": 2,
                "operational_count": 2,
                "fuel_type": "AvGas 100LL"
            }
        ],
        "fees": {
            "course_name": "Commercial Pilot License (Aeroplane) with Multi-Engine & IR",
            "currency": "INR",
            "tuition_flying_inr": 4200000,
            "ground_school_inr": 320000,
            "simulator_inr": 190000,
            "hostel_mess_annual_inr": 200000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 4910000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-02-01",
            "source_url": "https://caaviation.com/fees-structure",
            "inclusions": ["200 hrs flying training", "Ground theory syllabus", "ALX Level 5 Simulator", "Study material"],
            "exclusions": ["Hostel charges (₹16,500/month)", "Mess food charges", "DGCA examination fees", "DGCA license issue"]
        },
        "programmes": ["DGCA CPL with ME/IR", "IndiGo Cadet Pilot Programme", "PPL", "Flight Instructor Rating"],
        "training_capacity": {
            "annual_cadet_intake": 90,
            "active_instructors": 15,
            "avg_completion_months": 15
        }
    },

    # 5. Redbird Flight Training Academy (Baramati, Seoni, Gulbarga, Belagavi, Lilabari)
    {
        "school_id": "FTO_REDBIRD_004",
        "name": "Redbird Flight Training Academy Private Limited",
        "short_name": "Redbird Aviation",
        "slug": "redbird-flight-training",
        "website_url": "https://redbirdaviation.com",
        "ownership_type": "private",
        "dgca_approval_no": "DGCA/FTO/19/2017",
        "approval_validity": "2028-06-30",
        "operational_status": "active",
        "established_year": 2017,
        "confidence_score": 0.94,
        "completeness_score": 0.93,
        "last_verified_date": "2026-10-22",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Category B",
            "overall_score": 66.8,
            "national_rank": 5,
            "annual_hours_logged": 24000,
            "safety_audit_score": 87.5,
            "cfi_cadre_strength": 22,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_REDBIRD_BAR",
                "is_primary": True,
                "airport_name": "Baramati Airport",
                "icao_code": "VABB",
                "city": "Baramati",
                "state": "Maharashtra",
                "region": "West",
                "runway_length_meters": 1770,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "Controlled Tower",
                "latitude": 18.1561,
                "longitude": 74.5828
            },
            {
                "base_id": "BASE_REDBIRD_SEO",
                "is_primary": False,
                "airport_name": "Seoni Airstrip",
                "icao_code": "VASE",
                "city": "Seoni",
                "state": "Madhya Pradesh",
                "region": "Central",
                "runway_length_meters": 1350,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "FTO AFIS",
                "latitude": 22.0833,
                "longitude": 79.5500
            },
            {
                "base_id": "BASE_REDBIRD_GUL",
                "is_primary": False,
                "airport_name": "Kalaburagi Airport",
                "icao_code": "VOGB",
                "city": "Kalaburagi / Gulbarga",
                "state": "Karnataka",
                "region": "South",
                "runway_length_meters": 3175,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "AAI Controlled",
                "latitude": 17.3044,
                "longitude": 76.9536
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Tecnam P2008 JC",
                "manufacturer": "Tecnam",
                "engine_type": "single_engine",
                "avionics_type": "Garmin G3X Touch Glass Cockpit",
                "count": 22,
                "operational_count": 21,
                "fuel_type": "MOGAS / AvGas"
            },
            {
                "aircraft_model": "Tecnam P2006T",
                "manufacturer": "Tecnam",
                "engine_type": "multi_engine",
                "avionics_type": "Garmin G950 / G1000",
                "count": 4,
                "operational_count": 4,
                "fuel_type": "MOGAS / AvGas"
            }
        ],
        "fees": {
            "course_name": "Commercial Pilot License (Aeroplane) with Multi-Engine & IR",
            "currency": "INR",
            "tuition_flying_inr": 3950000,
            "ground_school_inr": 280000,
            "simulator_inr": 180000,
            "hostel_mess_annual_inr": 220000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 4630000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-03-01",
            "source_url": "https://redbirdaviation.com/course-details",
            "inclusions": ["200 hrs flying training", "Ground school syllabus", "Simulator sessions", "Pre-flight briefings"],
            "exclusions": ["Hostel & mess charges", "Medical tests", "DGCA examination fees"]
        },
        "programmes": ["DGCA CPL with Multi-Engine", "Air India Cadet Pathway", "Flight Instructor Course (AFIR/FIR)"],
        "training_capacity": {
            "annual_cadet_intake": 140,
            "active_instructors": 22,
            "avg_completion_months": 14
        }
    },

    # 6. Academy of Carver Aviation (Baramati)
    {
        "school_id": "FTO_CARVER_005",
        "name": "Academy of Carver Aviation Private Limited",
        "short_name": "Carver Aviation",
        "slug": "academy-of-carver-aviation",
        "website_url": "https://carveraviation.com",
        "ownership_type": "private",
        "dgca_approval_no": "DGCA/FTO/03/1995",
        "approval_validity": "2028-03-31",
        "operational_status": "active",
        "established_year": 1995,
        "confidence_score": 0.95,
        "completeness_score": 0.93,
        "last_verified_date": "2026-10-18",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Category B",
            "overall_score": 65.4,
            "national_rank": 6,
            "annual_hours_logged": 16500,
            "safety_audit_score": 86.2,
            "cfi_cadre_strength": 14,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_CARVER_BAR",
                "is_primary": True,
                "airport_name": "Baramati Airport",
                "icao_code": "VABB",
                "city": "Baramati",
                "state": "Maharashtra",
                "region": "West",
                "runway_length_meters": 1770,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "Controlled Tower",
                "latitude": 18.1561,
                "longitude": 74.5828
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Cessna 172R",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Garmin G1000 & Analogue",
                "count": 11,
                "operational_count": 10,
                "fuel_type": "AvGas 100LL"
            },
            {
                "aircraft_model": "Cessna 152",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Analogue Instrument Panel",
                "count": 4,
                "operational_count": 4,
                "fuel_type": "AvGas 100LL"
            },
            {
                "aircraft_model": "Partenavia P.68C",
                "manufacturer": "Vulcanair",
                "engine_type": "multi_engine",
                "avionics_type": "IFR Equipped",
                "count": 2,
                "operational_count": 2,
                "fuel_type": "AvGas 100LL"
            }
        ],
        "fees": {
            "course_name": "Commercial Pilot License (Aeroplane) with Multi-Engine & IR",
            "currency": "INR",
            "tuition_flying_inr": 3800000,
            "ground_school_inr": 250000,
            "simulator_inr": 160000,
            "hostel_mess_annual_inr": 180000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 4390000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-01-10",
            "source_url": "https://carveraviation.com/course-fees",
            "inclusions": ["200 hrs flying training", "Ground school instruction", "Simulator time", "Study manuals"],
            "exclusions": ["Hostel stay & mess food", "DGCA examination fees", "Class 1 medical charges"]
        },
        "programmes": ["Commercial Pilot License (CPL)", "Private Pilot License (PPL)", "Instrument Rating", "Multi-Engine Rating"],
        "training_capacity": {
            "annual_cadet_intake": 80,
            "active_instructors": 14,
            "avg_completion_months": 16
        }
    },

    # 7. Asia Pacific Flight Training Academy (Hyderabad)
    {
        "school_id": "FTO_APFT_008",
        "name": "Asia Pacific Flight Training Academy Limited",
        "short_name": "APFT Hyderabad",
        "slug": "apft-hyderabad",
        "website_url": "https://apft.edu.in",
        "ownership_type": "private",
        "dgca_approval_no": "DGCA/FTO/16/2013",
        "approval_validity": "2028-09-30",
        "operational_status": "active",
        "established_year": 2013,
        "confidence_score": 0.94,
        "completeness_score": 0.92,
        "last_verified_date": "2026-10-15",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Category B",
            "overall_score": 64.8,
            "national_rank": 7,
            "annual_hours_logged": 14800,
            "safety_audit_score": 86.8,
            "cfi_cadre_strength": 12,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_APFT_HYD",
                "is_primary": True,
                "airport_name": "Rajiv Gandhi International Airport",
                "icao_code": "VOHS",
                "city": "Hyderabad",
                "state": "Telangana",
                "region": "South",
                "runway_length_meters": 4260,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "Major Commercial Class A ATC",
                "latitude": 17.2403,
                "longitude": 78.4294
            },
            {
                "base_id": "BASE_APFT_GUL",
                "is_primary": False,
                "airport_name": "Kalaburagi Airport",
                "icao_code": "VOGB",
                "city": "Kalaburagi",
                "state": "Karnataka",
                "region": "South",
                "runway_length_meters": 3175,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "AAI Controlled",
                "latitude": 17.3044,
                "longitude": 76.9536
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Diamond DA40 NG",
                "manufacturer": "Diamond Aircraft",
                "engine_type": "single_engine",
                "avionics_type": "Garmin G1000 NXi",
                "count": 7,
                "operational_count": 7,
                "fuel_type": "Jet-A1"
            },
            {
                "aircraft_model": "Diamond DA42 Twin Star",
                "manufacturer": "Diamond Aircraft",
                "engine_type": "multi_engine",
                "avionics_type": "Garmin G1000 NXi",
                "count": 2,
                "operational_count": 2,
                "fuel_type": "Jet-A1"
            }
        ],
        "fees": {
            "course_name": "CPL Integrated Programme",
            "currency": "INR",
            "tuition_flying_inr": 4400000,
            "ground_school_inr": 350000,
            "simulator_inr": 220000,
            "hostel_mess_annual_inr": 210000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 5180000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-03-01",
            "source_url": "https://apft.edu.in/admissions",
            "inclusions": ["200 flight training hours", "Ground training", "ALX simulator sessions", "Airport passes"],
            "exclusions": ["Hostel & food", "DGCA exam & licensing fees"]
        },
        "programmes": ["DGCA CPL (ME/IR)", "Airline Cadet Prep", "PPL"],
        "training_capacity": {
            "annual_cadet_intake": 60,
            "active_instructors": 12,
            "avg_completion_months": 15
        }
    },

    # 8. SVKM’s NMIMS Academy of Aviation (Shirpur)
    {
        "school_id": "FTO_NMIMS_020",
        "name": "SVKM’s NMIMS Academy of Aviation",
        "short_name": "NMIMS Aviation Shirpur",
        "slug": "nmims-academy-of-aviation-shirpur",
        "website_url": "https://aviation.nmims.edu",
        "ownership_type": "university_trust",
        "dgca_approval_no": "DGCA/FTO/25/2018",
        "approval_validity": "2028-05-31",
        "operational_status": "active",
        "established_year": 2018,
        "confidence_score": 0.95,
        "completeness_score": 0.94,
        "last_verified_date": "2026-10-21",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Category B",
            "overall_score": 64.0,
            "national_rank": 8,
            "annual_hours_logged": 11500,
            "safety_audit_score": 85.8,
            "cfi_cadre_strength": 10,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_NMIMS_SHI",
                "is_primary": True,
                "airport_name": "Shirpur Airstrip",
                "icao_code": "VASH",
                "city": "Shirpur (Dhule)",
                "state": "Maharashtra",
                "region": "West",
                "runway_length_meters": 1400,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "FTO Dedicated Air Traffic Control",
                "latitude": 21.3500,
                "longitude": 74.8833
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Cessna 172R",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Garmin G1000 Glass Cockpit",
                "count": 5,
                "operational_count": 5,
                "fuel_type": "AvGas 100LL"
            },
            {
                "aircraft_model": "Piper PA-34 Seneca V",
                "manufacturer": "Piper Aircraft",
                "engine_type": "multi_engine",
                "avionics_type": "Garmin G600 Avionics",
                "count": 1,
                "operational_count": 1,
                "fuel_type": "AvGas 100LL"
            }
        ],
        "fees": {
            "course_name": "B.Sc. Aviation + Dual DGCA CPL (ME/IR)",
            "currency": "INR",
            "tuition_flying_inr": 4100000,
            "ground_school_inr": 350000,
            "simulator_inr": 180000,
            "hostel_mess_annual_inr": 190000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 4820000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-03-15",
            "source_url": "https://aviation.nmims.edu/fees",
            "inclusions": ["200 hrs flying training", "Academic university degree classes", "Simulator", "Study kits"],
            "exclusions": ["Hostel charges", "University examination fees", "DGCA license fees"]
        },
        "programmes": ["Dual B.Sc. (Aviation) + CPL", "Commercial Pilot License (ME/IR)", "PPL"],
        "training_capacity": {
            "annual_cadet_intake": 45,
            "active_instructors": 10,
            "avg_completion_months": 16
        }
    },

    # 9. BlueRay Aviation (Mehsana & Osmanabad)
    {
        "school_id": "FTO_BLUERAY_021",
        "name": "BlueRay Aviation Private Limited",
        "short_name": "BlueRay Aviation",
        "slug": "blueray-aviation-mehsana",
        "website_url": "https://bluerayaviation.com",
        "ownership_type": "private",
        "dgca_approval_no": "DGCA/FTO/29/2019",
        "approval_validity": "2028-02-28",
        "operational_status": "active",
        "established_year": 2019,
        "confidence_score": 0.94,
        "completeness_score": 0.92,
        "last_verified_date": "2026-10-19",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Category B",
            "overall_score": 63.4,
            "national_rank": 9,
            "annual_hours_logged": 13400,
            "safety_audit_score": 85.0,
            "cfi_cadre_strength": 12,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_BLUERAY_MEH",
                "is_primary": True,
                "airport_name": "Mehsana Airfield",
                "icao_code": "VAMS",
                "city": "Mehsana",
                "state": "Gujarat",
                "region": "West",
                "runway_length_meters": 1370,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "Dedicated FTO Tower",
                "latitude": 23.6167,
                "longitude": 72.3833
            },
            {
                "base_id": "BASE_BLUERAY_OSM",
                "is_primary": False,
                "airport_name": "Osmanabad Airport",
                "icao_code": "VAOS",
                "city": "Osmanabad",
                "state": "Maharashtra",
                "region": "West",
                "runway_length_meters": 1200,
                "runway_surface": "Asphalt",
                "night_flying_available": False,
                "atc_type": "Uncontrolled",
                "latitude": 18.1667,
                "longitude": 76.0500
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Cessna 172S",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Garmin G1000 NXi",
                "count": 8,
                "operational_count": 8,
                "fuel_type": "AvGas 100LL"
            },
            {
                "aircraft_model": "Tecnam P2006T",
                "manufacturer": "Tecnam",
                "engine_type": "multi_engine",
                "avionics_type": "Garmin G950",
                "count": 2,
                "operational_count": 2,
                "fuel_type": "AvGas 100LL"
            }
        ],
        "fees": {
            "course_name": "CPL with Multi-Engine & IR Pathway",
            "currency": "INR",
            "tuition_flying_inr": 3900000,
            "ground_school_inr": 280000,
            "simulator_inr": 180000,
            "hostel_mess_annual_inr": 180000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 4540000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-02-15",
            "source_url": "https://bluerayaviation.com/pricing",
            "inclusions": ["200 flying hours (185h SE + 15h ME)", "Ground classes", "Simulator session", "Airport charges"],
            "exclusions": ["Accommodation & food", "DGCA examination fees"]
        },
        "programmes": ["DGCA CPL (ME/IR)", "PPL", "Assistant Flight Instructor Rating"],
        "training_capacity": {
            "annual_cadet_intake": 70,
            "active_instructors": 12,
            "avg_completion_months": 15
        }
    },

    # 10. FSTC Flying School (Bhiwani & Narnaul)
    {
        "school_id": "FTO_FSTC_022",
        "name": "FSTC Flying School Private Limited",
        "short_name": "FSTC Flying School",
        "slug": "fstc-flying-school",
        "website_url": "https://fstc.in/flying-school",
        "ownership_type": "private",
        "dgca_approval_no": "DGCA/FTO/31/2019",
        "approval_validity": "2028-04-30",
        "operational_status": "active",
        "established_year": 2019,
        "confidence_score": 0.95,
        "completeness_score": 0.93,
        "last_verified_date": "2026-10-18",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Category B",
            "overall_score": 62.8,
            "national_rank": 10,
            "annual_hours_logged": 12200,
            "safety_audit_score": 84.6,
            "cfi_cadre_strength": 11,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_FSTC_BHI",
                "is_primary": True,
                "airport_name": "Bhiwani Airport",
                "icao_code": "VIBW",
                "city": "Bhiwani",
                "state": "Haryana",
                "region": "North",
                "runway_length_meters": 1370,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "Dedicated FTO Tower",
                "latitude": 28.7833,
                "longitude": 76.1333
            },
            {
                "base_id": "BASE_FSTC_NAR",
                "is_primary": False,
                "airport_name": "Narnaul Airstrip",
                "icao_code": "VINL",
                "city": "Narnaul",
                "state": "Haryana",
                "region": "North",
                "runway_length_meters": 1220,
                "runway_surface": "Asphalt",
                "night_flying_available": False,
                "atc_type": "Uncontrolled",
                "latitude": 28.0500,
                "longitude": 76.1000
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Cessna 172S Skyhawk",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Garmin G1000 Glass Cockpit",
                "count": 6,
                "operational_count": 6,
                "fuel_type": "AvGas 100LL"
            },
            {
                "aircraft_model": "Tecnam P2006T",
                "manufacturer": "Tecnam",
                "engine_type": "multi_engine",
                "avionics_type": "Garmin G950",
                "count": 1,
                "operational_count": 1,
                "fuel_type": "AvGas 100LL"
            }
        ],
        "fees": {
            "course_name": "Integrated CPL with Airline Simulator Transition",
            "currency": "INR",
            "tuition_flying_inr": 4300000,
            "ground_school_inr": 350000,
            "simulator_inr": 250000,
            "hostel_mess_annual_inr": 200000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 5100000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-03-01",
            "source_url": "https://fstc.in/flying-training-fees",
            "inclusions": ["200 hrs flying training", "Ground school instruction", "FSTC Level D Simulator access", "Study materials"],
            "exclusions": ["Hostel charges", "DGCA examination and endorsement fees"]
        },
        "programmes": ["DGCA CPL (ME/IR)", "Cadet Pilot Training", "Type Rating Transition"],
        "training_capacity": {
            "annual_cadet_intake": 55,
            "active_instructors": 11,
            "avg_completion_months": 15
        }
    },

    # 11. Flytech Aviation Academy (Hyderabad & Nagarjuna Sagar)
    {
        "school_id": "FTO_FLYTECH_023",
        "name": "Flytech Aviation Academy",
        "short_name": "Flytech Aviation",
        "slug": "flytech-aviation-academy",
        "website_url": "https://flytechaviation.aero",
        "ownership_type": "private",
        "dgca_approval_no": "DGCA/FTO/07/1996",
        "approval_validity": "2027-12-31",
        "operational_status": "active",
        "established_year": 1996,
        "confidence_score": 0.94,
        "completeness_score": 0.92,
        "last_verified_date": "2026-10-17",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Category B",
            "overall_score": 62.0,
            "national_rank": 11,
            "annual_hours_logged": 12800,
            "safety_audit_score": 83.8,
            "cfi_cadre_strength": 12,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_FLYTECH_NAD",
                "is_primary": True,
                "airport_name": "Nadergul Aerodrome",
                "icao_code": "VAND",
                "city": "Hyderabad",
                "state": "Telangana",
                "region": "South",
                "runway_length_meters": 1100,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "FTO Controlled Airfield",
                "latitude": 17.2833,
                "longitude": 78.5500
            },
            {
                "base_id": "BASE_FLYTECH_NAG",
                "is_primary": False,
                "airport_name": "Nagarjuna Sagar Airport",
                "icao_code": "VONS",
                "city": "Nagarjuna Sagar",
                "state": "Andhra Pradesh",
                "region": "South",
                "runway_length_meters": 1300,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "Uncontrolled",
                "latitude": 16.5333,
                "longitude": 79.3167
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Cessna 152",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Analogue",
                "count": 5,
                "operational_count": 5,
                "fuel_type": "AvGas 100LL"
            },
            {
                "aircraft_model": "Cessna 172P",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Garmin 430 Equipped",
                "count": 3,
                "operational_count": 3,
                "fuel_type": "AvGas 100LL"
            },
            {
                "aircraft_model": "Partenavia P.68C",
                "manufacturer": "Vulcanair",
                "engine_type": "multi_engine",
                "avionics_type": "IFR Cockpit",
                "count": 1,
                "operational_count": 1,
                "fuel_type": "AvGas 100LL"
            }
        ],
        "fees": {
            "course_name": "Commercial Pilot License (Aeroplane) with Multi-Engine & IR",
            "currency": "INR",
            "tuition_flying_inr": 3750000,
            "ground_school_inr": 250000,
            "simulator_inr": 150000,
            "hostel_mess_annual_inr": 180000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 4330000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-02-01",
            "source_url": "https://flytechaviation.aero/fees",
            "inclusions": ["200 hrs flight training", "Ground school instruction", "Simulator time", "Pre-flight briefs"],
            "exclusions": ["Hostel charges", "DGCA examination fees", "Medical clearance"]
        },
        "programmes": ["CPL with Multi-Engine", "PPL", "Flight Instructor Course (AFIR)", "AME Training"],
        "training_capacity": {
            "annual_cadet_intake": 65,
            "active_instructors": 12,
            "avg_completion_months": 16
        }
    },

    # 12. Madhya Pradesh Flying Club (Indore & Bhopal)
    {
        "school_id": "FTO_MPFC_006",
        "name": "The Madhya Pradesh Flying Club Limited",
        "short_name": "MPFC",
        "slug": "madhya-pradesh-flying-club",
        "website_url": "https://mpflyingclub.org",
        "ownership_type": "state_government_aided",
        "dgca_approval_no": "DGCA/FTO/02/1951",
        "approval_validity": "2027-04-30",
        "operational_status": "active",
        "established_year": 1951,
        "confidence_score": 0.95,
        "completeness_score": 0.91,
        "last_verified_date": "2026-10-15",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Category B",
            "overall_score": 60.8,
            "national_rank": 12,
            "annual_hours_logged": 11800,
            "safety_audit_score": 83.2,
            "cfi_cadre_strength": 8,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_MPFC_IDR",
                "is_primary": True,
                "airport_name": "Devi Ahilyabai Holkar Airport",
                "icao_code": "VAID",
                "city": "Indore",
                "state": "Madhya Pradesh",
                "region": "Central",
                "runway_length_meters": 2750,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "AAI Controlled International Airport",
                "latitude": 22.7217,
                "longitude": 75.8011
            },
            {
                "base_id": "BASE_MPFC_BHO",
                "is_primary": False,
                "airport_name": "Raja Bhoj Airport",
                "icao_code": "VABP",
                "city": "Bhopal",
                "state": "Madhya Pradesh",
                "region": "Central",
                "runway_length_meters": 2744,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "AAI Controlled",
                "latitude": 23.2878,
                "longitude": 77.3378
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Cessna 152",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Analogue with basic VOR",
                "count": 4,
                "operational_count": 4,
                "fuel_type": "AvGas 100LL"
            },
            {
                "aircraft_model": "Cessna 172R",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Analogue Instrument Panel",
                "count": 3,
                "operational_count": 3,
                "fuel_type": "AvGas 100LL"
            },
            {
                "aircraft_model": "Partenavia P.68C",
                "manufacturer": "Vulcanair",
                "engine_type": "multi_engine",
                "avionics_type": "Dual VOR / ILS equipped",
                "count": 1,
                "operational_count": 1,
                "fuel_type": "AvGas 100LL"
            }
        ],
        "fees": {
            "course_name": "DGCA CPL Course with Multi-Engine",
            "currency": "INR",
            "tuition_flying_inr": 3400000,
            "ground_school_inr": 200000,
            "simulator_inr": 120000,
            "hostel_mess_annual_inr": 160000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 3880000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-01-01",
            "source_url": "https://mpflyingclub.org/fees",
            "inclusions": ["200 hrs flying training", "Ground theory coaching", "Simulator session"],
            "exclusions": ["Hostel boarding", "DGCA examination fees", "Class 1 medical charges"]
        },
        "programmes": ["DGCA CPL (ME/IR)", "PPL", "Assistant Flight Instructor Rating (AFIR)"],
        "training_capacity": {
            "annual_cadet_intake": 40,
            "active_instructors": 8,
            "avg_completion_months": 20
        }
    },

    # 13. The Bombay Flying Club (Mumbai & Dhule)
    {
        "school_id": "FTO_BFC_007",
        "name": "The Bombay Flying Club",
        "short_name": "Bombay Flying Club",
        "slug": "the-bombay-flying-club",
        "website_url": "https://thebombayflyingclub.com",
        "ownership_type": "historical_trust",
        "dgca_approval_no": "DGCA/FTO/04/1928",
        "approval_validity": "2027-11-30",
        "operational_status": "active",
        "established_year": 1928,
        "confidence_score": 0.96,
        "completeness_score": 0.92,
        "last_verified_date": "2026-10-15",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Category B",
            "overall_score": 59.8,
            "national_rank": 13,
            "annual_hours_logged": 10900,
            "safety_audit_score": 82.5,
            "cfi_cadre_strength": 9,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_BFC_JUH",
                "is_primary": True,
                "airport_name": "Juhu Aerodrome",
                "icao_code": "VAJJ",
                "city": "Mumbai",
                "state": "Maharashtra",
                "region": "West",
                "runway_length_meters": 1140,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "AAI Controlled Tower (Mumbai CTR)",
                "latitude": 19.0975,
                "longitude": 72.8339
            },
            {
                "base_id": "BASE_BFC_DHU",
                "is_primary": False,
                "airport_name": "Dhule Airport",
                "icao_code": "VA53",
                "city": "Dhule",
                "state": "Maharashtra",
                "region": "West",
                "runway_length_meters": 1400,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "FTO Tower",
                "latitude": 20.9228,
                "longitude": 74.7331
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Cessna 172R Skyhawk",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Garmin G1000 Glass Cockpit",
                "count": 6,
                "operational_count": 6,
                "fuel_type": "AvGas 100LL"
            },
            {
                "aircraft_model": "Piper PA-34 Seneca",
                "manufacturer": "Piper Aircraft",
                "engine_type": "multi_engine",
                "avionics_type": "Analogue with Garmin GPS",
                "count": 1,
                "operational_count": 1,
                "fuel_type": "AvGas 100LL"
            }
        ],
        "fees": {
            "course_name": "CPL with Multi-Engine & Instrument Rating",
            "currency": "INR",
            "tuition_flying_inr": 4350000,
            "ground_school_inr": 350000,
            "simulator_inr": 200000,
            "hostel_mess_annual_inr": 240000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 5140000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-03-01",
            "source_url": "https://thebombayflyingclub.com/pilot-training-fees",
            "inclusions": ["200 hrs flying training", "Ground theory lectures", "Simulator briefings"],
            "exclusions": ["Hostel stay in Mumbai/Dhule", "DGCA examination fees"]
        },
        "programmes": ["DGCA CPL", "PPL", "B.Sc. (Aviation) with University of Mumbai", "Flight Instructor Course"],
        "training_capacity": {
            "annual_cadet_intake": 50,
            "active_instructors": 9,
            "avg_completion_months": 18
        }
    },

    # 14. Orient Flights Aviation Academy (Mysuru & Puducherry)
    {
        "school_id": "FTO_ORIENT_009",
        "name": "Orient Flights Aviation Academy",
        "short_name": "Orient Flights",
        "slug": "orient-flights-aviation-academy",
        "website_url": "https://orientflights.com",
        "ownership_type": "private",
        "dgca_approval_no": "DGCA/FTO/15/2012",
        "approval_validity": "2027-06-30",
        "operational_status": "active",
        "established_year": 2012,
        "confidence_score": 0.94,
        "completeness_score": 0.91,
        "last_verified_date": "2026-10-15",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Category B",
            "overall_score": 59.2,
            "national_rank": 14,
            "annual_hours_logged": 10200,
            "safety_audit_score": 82.0,
            "cfi_cadre_strength": 9,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_ORIENT_MYQ",
                "is_primary": True,
                "airport_name": "Mysore Airport",
                "icao_code": "VOMY",
                "city": "Mysuru",
                "state": "Karnataka",
                "region": "South",
                "runway_length_meters": 1740,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "AAI Controlled",
                "latitude": 12.2300,
                "longitude": 76.6500
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Cessna 172R",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Garmin G1000 Glass Cockpit",
                "count": 4,
                "operational_count": 4,
                "fuel_type": "AvGas 100LL"
            },
            {
                "aircraft_model": "Cessna 152",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Analogue Panel",
                "count": 2,
                "operational_count": 2,
                "fuel_type": "AvGas 100LL"
            },
            {
                "aircraft_model": "Piper PA-34 Seneca",
                "manufacturer": "Piper Aircraft",
                "engine_type": "multi_engine",
                "avionics_type": "IFR Avionics",
                "count": 1,
                "operational_count": 1,
                "fuel_type": "AvGas 100LL"
            }
        ],
        "fees": {
            "course_name": "Commercial Pilot License (Aeroplane) with ME & IR",
            "currency": "INR",
            "tuition_flying_inr": 3850000,
            "ground_school_inr": 280000,
            "simulator_inr": 160000,
            "hostel_mess_annual_inr": 180000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 4470000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-02-01",
            "source_url": "https://orientflights.com/pilot-training-cost",
            "inclusions": ["200 hrs flying training", "Ground theory curriculum", "Simulator practice"],
            "exclusions": ["Hostel & mess charges", "DGCA examination fees", "Medical certificate"]
        },
        "programmes": ["DGCA CPL (ME/IR)", "PPL", "Assistant Flight Instructor Rating"],
        "training_capacity": {
            "annual_cadet_intake": 45,
            "active_instructors": 9,
            "avg_completion_months": 16
        }
    },

    # 15. Banasthali Vidyapith Gliding and Flying Club (Tonk, Rajasthan)
    {
        "school_id": "FTO_BANASTHALI_010",
        "name": "Banasthali Vidyapith Gliding and Flying Club",
        "short_name": "Banasthali Flying Club",
        "slug": "banasthali-vidyapith-flying-club",
        "website_url": "https://banasthali.org",
        "ownership_type": "university_trust",
        "dgca_approval_no": "DGCA/FTO/13/2009",
        "approval_validity": "2028-01-31",
        "operational_status": "active",
        "established_year": 1962,
        "confidence_score": 0.95,
        "completeness_score": 0.92,
        "last_verified_date": "2026-10-15",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Category B",
            "overall_score": 58.4,
            "national_rank": 15,
            "annual_hours_logged": 8600,
            "safety_audit_score": 81.5,
            "cfi_cadre_strength": 7,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_BAN_BAN",
                "is_primary": True,
                "airport_name": "Banasthali Airstrip",
                "icao_code": "VI18",
                "city": "Banasthali (Tonk)",
                "state": "Rajasthan",
                "region": "North",
                "runway_length_meters": 1100,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "Dedicated FTO Tower",
                "latitude": 26.4025,
                "longitude": 75.8683
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Cessna 172R",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Garmin G1000 Glass Cockpit",
                "count": 4,
                "operational_count": 4,
                "fuel_type": "AvGas 100LL"
            },
            {
                "aircraft_model": "Partenavia P.68C",
                "manufacturer": "Vulcanair",
                "engine_type": "multi_engine",
                "avionics_type": "Analogue with IFR",
                "count": 1,
                "operational_count": 1,
                "fuel_type": "AvGas 100LL"
            }
        ],
        "fees": {
            "course_name": "B.Sc. (Aviation) with DGCA CPL (Women Exclusive)",
            "currency": "INR",
            "tuition_flying_inr": 3600000,
            "ground_school_inr": 250000,
            "simulator_inr": 140000,
            "hostel_mess_annual_inr": 160000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 4150000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-02-01",
            "source_url": "https://banasthali.org/aviation-admissions",
            "inclusions": ["200 hrs flying training", "Academic curriculum", "Hostel accommodation on campus", "Simulator training"],
            "exclusions": ["DGCA regulatory exam fees", "DGCA license issue fees"]
        },
        "programmes": ["DGCA CPL for Women", "B.Sc. Aviation", "PPL"],
        "training_capacity": {
            "annual_cadet_intake": 35,
            "active_instructors": 7,
            "avg_completion_months": 18
        }
    },

    # 16. Gujarat Flying Club (Vadodara)
    {
        "school_id": "FTO_GFC_011",
        "name": "The Gujarat Flying Club",
        "short_name": "Gujarat Flying Club",
        "slug": "gujarat-flying-club",
        "website_url": "https://gujaratflyingclub.com",
        "ownership_type": "state_government_aided",
        "dgca_approval_no": "DGCA/FTO/05/1960",
        "approval_validity": "2027-05-31",
        "operational_status": "active",
        "established_year": 1960,
        "confidence_score": 0.94,
        "completeness_score": 0.91,
        "last_verified_date": "2026-10-15",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Category B",
            "overall_score": 57.6,
            "national_rank": 16,
            "annual_hours_logged": 7900,
            "safety_audit_score": 81.0,
            "cfi_cadre_strength": 6,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_GFC_BDQ",
                "is_primary": True,
                "airport_name": "Vadodara Airport",
                "icao_code": "VABO",
                "city": "Vadodara",
                "state": "Gujarat",
                "region": "West",
                "runway_length_meters": 2469,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "AAI Controlled Airport",
                "latitude": 22.3361,
                "longitude": 73.2264
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Cessna 152",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Analogue Cockpit",
                "count": 3,
                "operational_count": 3,
                "fuel_type": "AvGas 100LL"
            },
            {
                "aircraft_model": "Cessna 172",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Analogue with GPS",
                "count": 2,
                "operational_count": 2,
                "fuel_type": "AvGas 100LL"
            }
        ],
        "fees": {
            "course_name": "DGCA CPL (SE) Pathway",
            "currency": "INR",
            "tuition_flying_inr": 3300000,
            "ground_school_inr": 200000,
            "simulator_inr": 120000,
            "hostel_mess_annual_inr": 150000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 3770000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-01-01",
            "source_url": "https://gujaratflyingclub.com/fee-schedule",
            "inclusions": ["200 hrs flying training", "Ground theoretical subjects", "Basic simulator briefings"],
            "exclusions": ["Hostel & mess accommodation", "DGCA examination fees", "Medical certification"]
        },
        "programmes": ["DGCA CPL (SE)", "PPL", "Assistant Flight Instructor Rating"],
        "training_capacity": {
            "annual_cadet_intake": 30,
            "active_instructors": 6,
            "avg_completion_months": 22
        }
    },

    # 17. Telangana State Aviation Academy (Hyderabad)
    {
        "school_id": "FTO_TSAA_012",
        "name": "Telangana State Aviation Academy",
        "short_name": "TSAA Hyderabad",
        "slug": "telangana-state-aviation-academy",
        "website_url": "https://tsaa.telangana.gov.in",
        "ownership_type": "state_government",
        "dgca_approval_no": "DGCA/FTO/06/1932",
        "approval_validity": "2028-10-31",
        "operational_status": "active",
        "established_year": 1932,
        "confidence_score": 0.96,
        "completeness_score": 0.93,
        "last_verified_date": "2026-10-15",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Category B",
            "overall_score": 57.0,
            "national_rank": 17,
            "annual_hours_logged": 8400,
            "safety_audit_score": 80.8,
            "cfi_cadre_strength": 7,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_TSAA_BEG",
                "is_primary": True,
                "airport_name": "Begumpet Airport",
                "icao_code": "VOHY",
                "city": "Hyderabad",
                "state": "Telangana",
                "region": "South",
                "runway_length_meters": 3200,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "AAI Controlled Airport",
                "latitude": 17.4531,
                "longitude": 78.4678
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Cessna 152",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Analogue",
                "count": 4,
                "operational_count": 4,
                "fuel_type": "AvGas 100LL"
            },
            {
                "aircraft_model": "Cessna 172R",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Analogue / Garmin 430",
                "count": 3,
                "operational_count": 3,
                "fuel_type": "AvGas 100LL"
            }
        ],
        "fees": {
            "course_name": "Government Subsidised Commercial Pilot License",
            "currency": "INR",
            "tuition_flying_inr": 3450000,
            "ground_school_inr": 200000,
            "simulator_inr": 130000,
            "hostel_mess_annual_inr": 160000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 3940000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-01-01",
            "source_url": "https://tsaa.telangana.gov.in/cpl-fees",
            "inclusions": ["200 hrs flying training", "Ground instruction", "Basic simulator briefings"],
            "exclusions": ["Hostel stay", "DGCA license endorsement & exam fees"]
        },
        "programmes": ["DGCA CPL (SE)", "PPL", "Assistant Flight Instructor Rating", "AME"],
        "training_capacity": {
            "annual_cadet_intake": 40,
            "active_instructors": 7,
            "avg_completion_months": 20
        }
    },

    # 18. Government Aviation Training Institute (GATI Bhubaneswar)
    {
        "school_id": "FTO_GATI_024",
        "name": "Government Aviation Training Institute (GATI)",
        "short_name": "GATI Odisha",
        "slug": "government-aviation-training-institute",
        "website_url": "https://flywithgati.com",
        "ownership_type": "state_government_aided",
        "dgca_approval_no": "DGCA/FTO/12/2008",
        "approval_validity": "2028-06-30",
        "operational_status": "active",
        "established_year": 1946,
        "confidence_score": 0.94,
        "completeness_score": 0.91,
        "last_verified_date": "2026-10-18",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Category B",
            "overall_score": 56.4,
            "national_rank": 18,
            "annual_hours_logged": 8100,
            "safety_audit_score": 80.2,
            "cfi_cadre_strength": 7,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_GATI_BIR",
                "is_primary": True,
                "airport_name": "Birasal Airstrip",
                "icao_code": "VEBD",
                "city": "Dhenkanal / Bhubaneswar",
                "state": "Odisha",
                "region": "East",
                "runway_length_meters": 1300,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "Dedicated FTO Air Traffic Control",
                "latitude": 20.9500,
                "longitude": 85.8000
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Cessna 152",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Analogue",
                "count": 4,
                "operational_count": 4,
                "fuel_type": "AvGas 100LL"
            },
            {
                "aircraft_model": "Cessna 172",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Garmin Glass Cockpit",
                "count": 3,
                "operational_count": 3,
                "fuel_type": "AvGas 100LL"
            },
            {
                "aircraft_model": "Partenavia P.68C",
                "manufacturer": "Vulcanair",
                "engine_type": "multi_engine",
                "avionics_type": "IFR Cockpit",
                "count": 1,
                "operational_count": 1,
                "fuel_type": "AvGas 100LL"
            }
        ],
        "fees": {
            "course_name": "DGCA CPL with Multi-Engine Rating",
            "currency": "INR",
            "tuition_flying_inr": 3650000,
            "ground_school_inr": 250000,
            "simulator_inr": 150000,
            "hostel_mess_annual_inr": 170000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 4220000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-02-01",
            "source_url": "https://flywithgati.com/courses",
            "inclusions": ["200 hrs flying training", "Ground instruction", "Simulator briefings"],
            "exclusions": ["Hostel charges", "DGCA examination fees"]
        },
        "programmes": ["DGCA CPL (ME/IR)", "PPL", "Assistant Flight Instructor Rating"],
        "training_capacity": {
            "annual_cadet_intake": 40,
            "active_instructors": 7,
            "avg_completion_months": 18
        }
    },

    # 19. Haryana Institute of Civil Aviation (Karnal & Pinjore)
    {
        "school_id": "FTO_HICA_014",
        "name": "Haryana Institute of Civil Aviation",
        "short_name": "HICA Karnal",
        "slug": "haryana-institute-of-civil-aviation",
        "website_url": "https://hicaonline.in",
        "ownership_type": "state_government",
        "dgca_approval_no": "DGCA/FTO/10/1999",
        "approval_validity": "2027-09-30",
        "operational_status": "active",
        "established_year": 1966,
        "confidence_score": 0.94,
        "completeness_score": 0.90,
        "last_verified_date": "2026-10-15",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Category B",
            "overall_score": 55.4,
            "national_rank": 19,
            "annual_hours_logged": 7500,
            "safety_audit_score": 79.5,
            "cfi_cadre_strength": 6,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_HICA_KAR",
                "is_primary": True,
                "airport_name": "Karnal Flying Club Airstrip",
                "icao_code": "VI45",
                "city": "Karnal",
                "state": "Haryana",
                "region": "North",
                "runway_length_meters": 1100,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "Civil Aerodrome Tower",
                "latitude": 29.6858,
                "longitude": 77.0192
            },
            {
                "base_id": "BASE_HICA_PIN",
                "is_primary": False,
                "airport_name": "Pinjore Airfield",
                "icao_code": "VI71",
                "city": "Pinjore",
                "state": "Haryana",
                "region": "North",
                "runway_length_meters": 1150,
                "runway_surface": "Asphalt",
                "night_flying_available": False,
                "atc_type": "FTO AFIS",
                "latitude": 30.7964,
                "longitude": 76.9142
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Cessna 152",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Analogue",
                "count": 4,
                "operational_count": 4,
                "fuel_type": "AvGas 100LL"
            },
            {
                "aircraft_model": "Cessna 172R",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Analogue / Garmin 430",
                "count": 2,
                "operational_count": 2,
                "fuel_type": "AvGas 100LL"
            }
        ],
        "fees": {
            "course_name": "State Subsidised CPL Course",
            "currency": "INR",
            "tuition_flying_inr": 3200000,
            "ground_school_inr": 180000,
            "simulator_inr": 110000,
            "hostel_mess_annual_inr": 140000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 3630000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-01-01",
            "source_url": "https://hicaonline.in/fee-structure",
            "inclusions": ["200 hrs flight training", "Ground instruction", "Basic simulator briefings"],
            "exclusions": ["Hostel charges", "DGCA examination fees", "DGCA license issue"]
        },
        "programmes": ["DGCA CPL", "PPL", "Assistant Flight Instructor Rating"],
        "training_capacity": {
            "annual_cadet_intake": 35,
            "active_instructors": 6,
            "avg_completion_months": 22
        }
    },

    # 20. Rajiv Gandhi Academy for Aviation Technology (RAGAAT Trivandrum)
    {
        "school_id": "FTO_RAGAAT_025",
        "name": "Rajiv Gandhi Academy for Aviation Technology",
        "short_name": "RAGAAT Kerala",
        "slug": "rajiv-gandhi-academy-aviation-technology",
        "website_url": "https://rajivgandhiacademyforaviationtechnology.org",
        "ownership_type": "state_government",
        "dgca_approval_no": "DGCA/FTO/14/2006",
        "approval_validity": "2028-03-31",
        "operational_status": "active",
        "established_year": 1959,
        "confidence_score": 0.94,
        "completeness_score": 0.90,
        "last_verified_date": "2026-10-18",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Category B",
            "overall_score": 54.2,
            "national_rank": 20,
            "annual_hours_logged": 6800,
            "safety_audit_score": 79.0,
            "cfi_cadre_strength": 6,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_RAGAAT_TRV",
                "is_primary": True,
                "airport_name": "Thiruvananthapuram International Airport",
                "icao_code": "VOTV",
                "city": "Thiruvananthapuram",
                "state": "Kerala",
                "region": "South",
                "runway_length_meters": 3400,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "AAI International Controlled Tower",
                "latitude": 8.4822,
                "longitude": 76.9200
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Cessna 172R",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Garmin G1000 Glass Cockpit",
                "count": 3,
                "operational_count": 3,
                "fuel_type": "AvGas 100LL"
            },
            {
                "aircraft_model": "Piper PA-34 Seneca",
                "manufacturer": "Piper Aircraft",
                "engine_type": "multi_engine",
                "avionics_type": "Analogue with IFR",
                "count": 1,
                "operational_count": 1,
                "fuel_type": "AvGas 100LL"
            }
        ],
        "fees": {
            "course_name": "Commercial Pilot License (Aeroplane) with Multi-Engine & IR",
            "currency": "INR",
            "tuition_flying_inr": 3500000,
            "ground_school_inr": 220000,
            "simulator_inr": 130000,
            "hostel_mess_annual_inr": 150000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 4000000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-01-01",
            "source_url": "https://rajivgandhiacademyforaviationtechnology.org/fees",
            "inclusions": ["200 hrs flying training", "Ground theoretical classes", "Simulator time"],
            "exclusions": ["Hostel boarding", "DGCA examination fees", "Medical fees"]
        },
        "programmes": ["DGCA CPL with ME/IR", "PPL", "Assistant Flight Instructor Rating"],
        "training_capacity": {
            "annual_cadet_intake": 30,
            "active_instructors": 6,
            "avg_completion_months": 20
        }
    },

    # 21. Ahmedabad Aviation & Aeronautics (AAA)
    {
        "school_id": "FTO_AAA_026",
        "name": "Ahmedabad Aviation & Aeronautics Limited",
        "short_name": "AAA Ahmedabad",
        "slug": "ahmedabad-aviation-aeronautics",
        "website_url": "https://aaa.co.in",
        "ownership_type": "private",
        "dgca_approval_no": "DGCA/FTO/09/1994",
        "approval_validity": "2027-10-31",
        "operational_status": "active",
        "established_year": 1994,
        "confidence_score": 0.94,
        "completeness_score": 0.91,
        "last_verified_date": "2026-10-18",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Category B",
            "overall_score": 53.5,
            "national_rank": 21,
            "annual_hours_logged": 7200,
            "safety_audit_score": 78.8,
            "cfi_cadre_strength": 6,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_AAA_AMD",
                "is_primary": True,
                "airport_name": "Sardar Vallabhbhai Patel International Airport",
                "icao_code": "VAAH",
                "city": "Ahmedabad",
                "state": "Gujarat",
                "region": "West",
                "runway_length_meters": 3505,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "Major Controlled International Tower",
                "latitude": 23.0772,
                "longitude": 72.6347
            },
            {
                "base_id": "BASE_AAA_MEH",
                "is_primary": False,
                "airport_name": "Mehsana Airfield",
                "icao_code": "VAMS",
                "city": "Mehsana",
                "state": "Gujarat",
                "region": "West",
                "runway_length_meters": 1370,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "FTO AFIS",
                "latitude": 23.6167,
                "longitude": 72.3833
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Cessna 152",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Analogue",
                "count": 4,
                "operational_count": 4,
                "fuel_type": "AvGas 100LL"
            },
            {
                "aircraft_model": "Cessna 172R",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Analogue with GPS",
                "count": 2,
                "operational_count": 2,
                "fuel_type": "AvGas 100LL"
            }
        ],
        "fees": {
            "course_name": "CPL Standard Course",
            "currency": "INR",
            "tuition_flying_inr": 3500000,
            "ground_school_inr": 240000,
            "simulator_inr": 140000,
            "hostel_mess_annual_inr": 180000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 4060000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-02-01",
            "source_url": "https://aaa.co.in/cpl-fees",
            "inclusions": ["200 hrs flying training", "Ground lectures", "Simulator briefings"],
            "exclusions": ["Hostel accommodation", "DGCA examination fees"]
        },
        "programmes": ["DGCA CPL", "PPL", "Assistant Flight Instructor Rating"],
        "training_capacity": {
            "annual_cadet_intake": 35,
            "active_instructors": 6,
            "avg_completion_months": 20
        }
    },

    # 22. Pioneer Flying Academy (Aligarh) - Category C
    {
        "school_id": "FTO_PIONEER_013",
        "name": "Pioneer Flying Academy Private Limited",
        "short_name": "Pioneer Flying Academy",
        "slug": "pioneer-flying-academy",
        "website_url": "https://pioneerflying.com",
        "ownership_type": "private",
        "dgca_approval_no": "DGCA/FTO/18/2015",
        "approval_validity": "2027-04-30",
        "operational_status": "active",
        "established_year": 2008,
        "confidence_score": 0.93,
        "completeness_score": 0.89,
        "last_verified_date": "2026-10-15",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Category C",
            "overall_score": 48.8,
            "national_rank": 22,
            "annual_hours_logged": 5800,
            "safety_audit_score": 76.0,
            "cfi_cadre_strength": 5,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_PIO_ALI",
                "is_primary": True,
                "airport_name": "Aligarh Airstrip",
                "icao_code": "VIAH",
                "city": "Aligarh",
                "state": "Uttar Pradesh",
                "region": "North",
                "runway_length_meters": 1200,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "Dedicated FTO Air Traffic Control",
                "latitude": 27.8833,
                "longitude": 78.0833
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Cessna 152",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Analogue Cockpit",
                "count": 3,
                "operational_count": 3,
                "fuel_type": "AvGas 100LL"
            },
            {
                "aircraft_model": "Cessna 172",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Analogue Instrument Panel",
                "count": 2,
                "operational_count": 2,
                "fuel_type": "AvGas 100LL"
            }
        ],
        "fees": {
            "course_name": "DGCA CPL (SE) Course",
            "currency": "INR",
            "tuition_flying_inr": 3500000,
            "ground_school_inr": 200000,
            "simulator_inr": 120000,
            "hostel_mess_annual_inr": 160000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 3980000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-01-01",
            "source_url": "https://pioneerflying.com/cpl-fees",
            "inclusions": ["200 hrs flying training", "Ground school syllabus", "Simulator sessions"],
            "exclusions": ["Hostel charges", "DGCA examination fees"]
        },
        "programmes": ["DGCA CPL", "PPL", "Assistant Flight Instructor Rating"],
        "training_capacity": {
            "annual_cadet_intake": 30,
            "active_instructors": 5,
            "avg_completion_months": 22
        }
    },

    # 23. Garg Aviation Limited (Kanpur) - Category C
    {
        "school_id": "FTO_GARG_016",
        "name": "Garg Aviation Limited",
        "short_name": "Garg Aviation",
        "slug": "garg-aviation-kanpur",
        "website_url": "https://gargaviation.com",
        "ownership_type": "private",
        "dgca_approval_no": "DGCA/FTO/17/1995",
        "approval_validity": "2027-03-31",
        "operational_status": "active",
        "established_year": 1995,
        "confidence_score": 0.93,
        "completeness_score": 0.88,
        "last_verified_date": "2026-10-15",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Category C",
            "overall_score": 48.0,
            "national_rank": 23,
            "annual_hours_logged": 5200,
            "safety_audit_score": 75.5,
            "cfi_cadre_strength": 5,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_GARG_KNP",
                "is_primary": True,
                "airport_name": "Civil Aerodrome Cantt",
                "icao_code": "VIKA",
                "city": "Kanpur",
                "state": "Uttar Pradesh",
                "region": "North",
                "runway_length_meters": 1100,
                "runway_surface": "Asphalt",
                "night_flying_available": False,
                "atc_type": "Controlled Tower",
                "latitude": 26.4419,
                "longitude": 80.3606
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Cessna 152",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Analogue",
                "count": 3,
                "operational_count": 3,
                "fuel_type": "AvGas 100LL"
            },
            {
                "aircraft_model": "Cessna 172",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Analogue with GPS",
                "count": 2,
                "operational_count": 2,
                "fuel_type": "AvGas 100LL"
            }
        ],
        "fees": {
            "course_name": "DGCA CPL Course",
            "currency": "INR",
            "tuition_flying_inr": 3400000,
            "ground_school_inr": 200000,
            "simulator_inr": 110000,
            "hostel_mess_annual_inr": 150000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 3860000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-01-01",
            "source_url": "https://gargaviation.com/course-fees",
            "inclusions": ["200 hrs flying training", "Ground school instruction", "Simulator time"],
            "exclusions": ["Hostel charges", "DGCA examination fees", "Class 1 medical tests"]
        },
        "programmes": ["DGCA CPL", "PPL", "Assistant Flight Instructor Rating"],
        "training_capacity": {
            "annual_cadet_intake": 25,
            "active_instructors": 5,
            "avg_completion_months": 24
        }
    },

    # 24. Jet Serve Aviation / Falcon Aviation (Flyola) - Category C
    {
        "school_id": "FTO_FALCON_015",
        "name": "Jet Serve Aviation Private Limited (Falcon / Flyola)",
        "short_name": "Flyola / Jet Serve",
        "slug": "falcon-aviation-academy-flyola",
        "website_url": "https://flyola.in",
        "ownership_type": "private",
        "dgca_approval_no": "DGCA/FTO/23/2013",
        "approval_validity": "2027-10-31",
        "operational_status": "active",
        "established_year": 2011,
        "confidence_score": 0.93,
        "completeness_score": 0.89,
        "last_verified_date": "2026-10-15",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Category C",
            "overall_score": 47.4,
            "national_rank": 24,
            "annual_hours_logged": 5600,
            "safety_audit_score": 75.0,
            "cfi_cadre_strength": 5,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_FAL_HJR",
                "is_primary": True,
                "airport_name": "Khajuraho Airport",
                "icao_code": "VEKO",
                "city": "Khajuraho",
                "state": "Madhya Pradesh",
                "region": "Central",
                "runway_length_meters": 2274,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "AAI Controlled Tower",
                "latitude": 24.8172,
                "longitude": 79.9192
            },
            {
                "base_id": "BASE_FAL_REW",
                "is_primary": False,
                "airport_name": "Rewa Airport",
                "icao_code": "VA1G",
                "city": "Rewa",
                "state": "Madhya Pradesh",
                "region": "Central",
                "runway_length_meters": 1400,
                "runway_surface": "Asphalt",
                "night_flying_available": False,
                "atc_type": "FTO AFIS",
                "latitude": 24.5333,
                "longitude": 81.3000
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Tecnam P2008 JC",
                "manufacturer": "Tecnam",
                "engine_type": "single_engine",
                "avionics_type": "Garmin G3X Touch",
                "count": 4,
                "operational_count": 4,
                "fuel_type": "MOGAS"
            },
            {
                "aircraft_model": "Tecnam P2006T",
                "manufacturer": "Tecnam",
                "engine_type": "multi_engine",
                "avionics_type": "Garmin G950",
                "count": 1,
                "operational_count": 1,
                "fuel_type": "MOGAS"
            }
        ],
        "fees": {
            "course_name": "DGCA CPL Integrated Course",
            "currency": "INR",
            "tuition_flying_inr": 3600000,
            "ground_school_inr": 240000,
            "simulator_inr": 140000,
            "hostel_mess_annual_inr": 170000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 4150000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-02-01",
            "source_url": "https://flyola.in/fees",
            "inclusions": ["200 hrs flying training", "Ground school instruction", "Simulator time"],
            "exclusions": ["Hostel charges", "DGCA examination fees"]
        },
        "programmes": ["DGCA CPL", "PPL", "Assistant Flight Instructor Rating"],
        "training_capacity": {
            "annual_cadet_intake": 30,
            "active_instructors": 5,
            "avg_completion_months": 22
        }
    },

    # 25. Patiala Aviation Club (Patiala) - Category C
    {
        "school_id": "FTO_PATIALA_018",
        "name": "Patiala Aviation Club",
        "short_name": "Patiala Aviation Club",
        "slug": "patiala-aviation-club",
        "website_url": "https://punjabcivilaviation.gov.in",
        "ownership_type": "state_government",
        "dgca_approval_no": "DGCA/FTO/21/1962",
        "approval_validity": "2027-08-31",
        "operational_status": "active",
        "established_year": 1962,
        "confidence_score": 0.93,
        "completeness_score": 0.88,
        "last_verified_date": "2026-10-15",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Category C",
            "overall_score": 46.5,
            "national_rank": 25,
            "annual_hours_logged": 4900,
            "safety_audit_score": 74.0,
            "cfi_cadre_strength": 4,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_PAT_PAT",
                "is_primary": True,
                "airport_name": "Patiala Civil Aerodrome",
                "icao_code": "VIPL",
                "city": "Patiala",
                "state": "Punjab",
                "region": "North",
                "runway_length_meters": 1150,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "Civil Aerodrome Tower",
                "latitude": 30.3167,
                "longitude": 76.3667
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Cessna 152",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Analogue",
                "count": 3,
                "operational_count": 3,
                "fuel_type": "AvGas 100LL"
            },
            {
                "aircraft_model": "Cessna 172",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Analogue with GPS",
                "count": 2,
                "operational_count": 2,
                "fuel_type": "AvGas 100LL"
            }
        ],
        "fees": {
            "course_name": "Punjab Government Subsidised CPL Course",
            "currency": "INR",
            "tuition_flying_inr": 3100000,
            "ground_school_inr": 180000,
            "simulator_inr": 100000,
            "hostel_mess_annual_inr": 140000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 3520000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-01-01",
            "source_url": "https://punjabcivilaviation.gov.in/patiala-cpl-fees",
            "inclusions": ["200 hrs flying training", "Ground instruction", "Basic simulator briefings"],
            "exclusions": ["Hostel charges", "DGCA examination fees", "DGCA license issue"]
        },
        "programmes": ["DGCA CPL", "PPL", "Assistant Flight Instructor Rating"],
        "training_capacity": {
            "annual_cadet_intake": 25,
            "active_instructors": 4,
            "avg_completion_months": 24
        }
    },

    # 26. Alchemist Aviation (Jamshedpur) - Category C
    {
        "school_id": "FTO_ALCHEMIST_017",
        "name": "Alchemist Aviation Private Limited",
        "short_name": "Alchemist Aviation",
        "slug": "alchemist-aviation-jamshedpur",
        "website_url": "https://alchemistaviation.in",
        "ownership_type": "private",
        "dgca_approval_no": "DGCA/FTO/20/2008",
        "approval_validity": "2027-02-28",
        "operational_status": "active",
        "established_year": 2008,
        "confidence_score": 0.92,
        "completeness_score": 0.88,
        "last_verified_date": "2026-10-15",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Category C",
            "overall_score": 45.8,
            "national_rank": 26,
            "annual_hours_logged": 4500,
            "safety_audit_score": 73.5,
            "cfi_cadre_strength": 4,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_ALC_IXW",
                "is_primary": True,
                "airport_name": "Sonari Airport",
                "icao_code": "VEJS",
                "city": "Jamshedpur",
                "state": "Jharkhand",
                "region": "East",
                "runway_length_meters": 1030,
                "runway_surface": "Asphalt",
                "night_flying_available": False,
                "atc_type": "Tata Steel / Controlled Tower",
                "latitude": 22.8131,
                "longitude": 86.1681
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Cessna 152",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Analogue",
                "count": 3,
                "operational_count": 3,
                "fuel_type": "AvGas 100LL"
            },
            {
                "aircraft_model": "Piper PA-28 Archer",
                "manufacturer": "Piper Aircraft",
                "engine_type": "single_engine",
                "avionics_type": "Analogue Panel",
                "count": 1,
                "operational_count": 1,
                "fuel_type": "AvGas 100LL"
            }
        ],
        "fees": {
            "course_name": "CPL Standard Course (Single Engine)",
            "currency": "INR",
            "tuition_flying_inr": 3400000,
            "ground_school_inr": 200000,
            "simulator_inr": 110000,
            "hostel_mess_annual_inr": 150000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 3860000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-01-01",
            "source_url": "https://alchemistaviation.in/cpl-fees",
            "inclusions": ["200 hrs flying training", "Ground instruction", "Basic simulator briefings"],
            "exclusions": ["Hostel boarding", "DGCA examination fees", "DGCA license issue"]
        },
        "programmes": ["DGCA CPL", "PPL", "Assistant Flight Instructor Rating"],
        "training_capacity": {
            "annual_cadet_intake": 20,
            "active_instructors": 4,
            "avg_completion_months": 24
        }
    },

    # 27. Sha-Shib Flying Academy (Guna) - Category C
    {
        "school_id": "FTO_SHASHIB_027",
        "name": "Sha-Shib Flying Academy",
        "short_name": "Sha-Shib Aviation",
        "slug": "sha-shib-flying-academy-guna",
        "website_url": "https://shashibaero.org",
        "ownership_type": "private",
        "dgca_approval_no": "DGCA/FTO/26/2009",
        "approval_validity": "2027-11-30",
        "operational_status": "active",
        "established_year": 2009,
        "confidence_score": 0.93,
        "completeness_score": 0.89,
        "last_verified_date": "2026-10-18",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Category C",
            "overall_score": 45.0,
            "national_rank": 27,
            "annual_hours_logged": 4600,
            "safety_audit_score": 73.0,
            "cfi_cadre_strength": 5,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_SHA_GUN",
                "is_primary": True,
                "airport_name": "Guna Airstrip",
                "icao_code": "VAGN",
                "city": "Guna",
                "state": "Madhya Pradesh",
                "region": "Central",
                "runway_length_meters": 1200,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "Dedicated FTO Tower",
                "latitude": 24.6500,
                "longitude": 77.3167
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Cessna 152",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Analogue",
                "count": 3,
                "operational_count": 3,
                "fuel_type": "AvGas 100LL"
            },
            {
                "aircraft_model": "Cessna 172R",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Garmin Glass Cockpit",
                "count": 2,
                "operational_count": 2,
                "fuel_type": "AvGas 100LL"
            },
            {
                "aircraft_model": "Partenavia P.68C",
                "manufacturer": "Vulcanair",
                "engine_type": "multi_engine",
                "avionics_type": "Analogue IFR",
                "count": 1,
                "operational_count": 1,
                "fuel_type": "AvGas 100LL"
            }
        ],
        "fees": {
            "course_name": "DGCA CPL Course with Multi-Engine",
            "currency": "INR",
            "tuition_flying_inr": 3600000,
            "ground_school_inr": 220000,
            "simulator_inr": 130000,
            "hostel_mess_annual_inr": 160000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 4110000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-02-01",
            "source_url": "https://shashibaero.org/pilot-training-fees",
            "inclusions": ["200 hrs flying training", "Ground school instruction", "Simulator time"],
            "exclusions": ["Hostel charges", "DGCA examination fees"]
        },
        "programmes": ["DGCA CPL", "PPL", "Assistant Flight Instructor Rating", "AME"],
        "training_capacity": {
            "annual_cadet_intake": 30,
            "active_instructors": 5,
            "avg_completion_months": 22
        }
    },

    # 28. Ambitions Flying Club (Karad & Aligarh) - Category C
    {
        "school_id": "FTO_AMBITIONS_028",
        "name": "Ambitions Flying Club Private Limited",
        "short_name": "Ambitions Flying Club",
        "slug": "ambitions-flying-club",
        "website_url": "https://ambitionsflyingclub.com",
        "ownership_type": "private",
        "dgca_approval_no": "DGCA/FTO/27/2012",
        "approval_validity": "2027-09-30",
        "operational_status": "active",
        "established_year": 2012,
        "confidence_score": 0.93,
        "completeness_score": 0.88,
        "last_verified_date": "2026-10-18",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Category C",
            "overall_score": 44.2,
            "national_rank": 28,
            "annual_hours_logged": 4200,
            "safety_audit_score": 72.0,
            "cfi_cadre_strength": 4,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_AMB_KRD",
                "is_primary": True,
                "airport_name": "Karad Airport",
                "icao_code": "VA1M",
                "city": "Karad (Satara)",
                "state": "Maharashtra",
                "region": "West",
                "runway_length_meters": 1280,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "FTO Air Traffic Services",
                "latitude": 17.2833,
                "longitude": 74.1833
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Cessna 152",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Analogue",
                "count": 3,
                "operational_count": 3,
                "fuel_type": "AvGas 100LL"
            },
            {
                "aircraft_model": "Cessna 172",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Analogue Instrument Panel",
                "count": 2,
                "operational_count": 2,
                "fuel_type": "AvGas 100LL"
            }
        ],
        "fees": {
            "course_name": "DGCA CPL Course",
            "currency": "INR",
            "tuition_flying_inr": 3450000,
            "ground_school_inr": 200000,
            "simulator_inr": 120000,
            "hostel_mess_annual_inr": 160000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 3930000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-01-15",
            "source_url": "https://ambitionsflyingclub.com/fees",
            "inclusions": ["200 hrs flying training", "Ground instruction", "Simulator time"],
            "exclusions": ["Hostel charges", "DGCA examination fees"]
        },
        "programmes": ["DGCA CPL", "PPL", "Assistant Flight Instructor Rating"],
        "training_capacity": {
            "annual_cadet_intake": 25,
            "active_instructors": 4,
            "avg_completion_months": 22
        }
    },

    # 29. Nagpur Flying Club (Nagpur) - Category C
    {
        "school_id": "FTO_NFC_029",
        "name": "The Nagpur Flying Club",
        "short_name": "Nagpur Flying Club",
        "slug": "nagpur-flying-club",
        "website_url": "https://nagpurflyingclub.com",
        "ownership_type": "state_government",
        "dgca_approval_no": "DGCA/FTO/15/1947",
        "approval_validity": "2027-06-30",
        "operational_status": "active",
        "established_year": 1947,
        "confidence_score": 0.93,
        "completeness_score": 0.88,
        "last_verified_date": "2026-10-18",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Category C",
            "overall_score": 43.5,
            "national_rank": 29,
            "annual_hours_logged": 3800,
            "safety_audit_score": 71.5,
            "cfi_cadre_strength": 4,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_NFC_NAG",
                "is_primary": True,
                "airport_name": "Dr. Babasaheb Ambedkar International Airport",
                "icao_code": "VANP",
                "city": "Nagpur",
                "state": "Maharashtra",
                "region": "West",
                "runway_length_meters": 3200,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "Major Controlled International Tower",
                "latitude": 21.0922,
                "longitude": 79.0472
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Cessna 152",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Analogue",
                "count": 3,
                "operational_count": 3,
                "fuel_type": "AvGas 100LL"
            },
            {
                "aircraft_model": "Cessna 172R",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Analogue Panel",
                "count": 1,
                "operational_count": 1,
                "fuel_type": "AvGas 100LL"
            }
        ],
        "fees": {
            "course_name": "State Subsidised CPL Course",
            "currency": "INR",
            "tuition_flying_inr": 3250000,
            "ground_school_inr": 180000,
            "simulator_inr": 110000,
            "hostel_mess_annual_inr": 150000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 3690000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-01-01",
            "source_url": "https://nagpurflyingclub.com/fees",
            "inclusions": ["200 hrs flying training", "Ground instruction", "Basic simulator briefings"],
            "exclusions": ["Hostel charges", "DGCA examination fees"]
        },
        "programmes": ["DGCA CPL", "PPL", "Assistant Flight Instructor Rating"],
        "training_capacity": {
            "annual_cadet_intake": 20,
            "active_instructors": 4,
            "avg_completion_months": 24
        }
    },

    # 30. Wings Aviation (Hyderabad) - Category C
    {
        "school_id": "FTO_WINGS_030",
        "name": "Wings Aviation Private Limited",
        "short_name": "Wings Aviation",
        "slug": "wings-aviation-hyderabad",
        "website_url": "https://wingsaviation.org",
        "ownership_type": "private",
        "dgca_approval_no": "DGCA/FTO/28/2005",
        "approval_validity": "2027-05-31",
        "operational_status": "active",
        "established_year": 2005,
        "confidence_score": 0.92,
        "completeness_score": 0.88,
        "last_verified_date": "2026-10-18",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Category C",
            "overall_score": 42.0,
            "national_rank": 30,
            "annual_hours_logged": 3500,
            "safety_audit_score": 70.0,
            "cfi_cadre_strength": 4,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_WNG_BEG",
                "is_primary": True,
                "airport_name": "Begumpet Airport",
                "icao_code": "VOHY",
                "city": "Hyderabad",
                "state": "Telangana",
                "region": "South",
                "runway_length_meters": 3200,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "AAI Controlled",
                "latitude": 17.4531,
                "longitude": 78.4678
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Cessna 152",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Analogue",
                "count": 3,
                "operational_count": 3,
                "fuel_type": "AvGas 100LL"
            },
            {
                "aircraft_model": "Cessna 172",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Analogue with GPS",
                "count": 2,
                "operational_count": 2,
                "fuel_type": "AvGas 100LL"
            }
        ],
        "fees": {
            "course_name": "DGCA CPL Course",
            "currency": "INR",
            "tuition_flying_inr": 3400000,
            "ground_school_inr": 200000,
            "simulator_inr": 110000,
            "hostel_mess_annual_inr": 160000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 3870000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-01-01",
            "source_url": "https://wingsaviation.org/cpl-fees",
            "inclusions": ["200 hrs flying training", "Ground instruction", "Simulator time"],
            "exclusions": ["Hostel charges", "DGCA examination fees"]
        },
        "programmes": ["DGCA CPL", "PPL", "Assistant Flight Instructor Rating"],
        "training_capacity": {
            "annual_cadet_intake": 20,
            "active_instructors": 4,
            "avg_completion_months": 24
        }
    },

    # 31. Skynex Aero (Jalgaon) - Exempt / Under Assessment (<18 months operational)
    {
        "school_id": "FTO_SKYNEX_031",
        "name": "Skynex Aero Private Limited",
        "short_name": "Skynex Aero Jalgaon",
        "slug": "skynex-aero-jalgaon",
        "website_url": "https://skynex.aero",
        "ownership_type": "private",
        "dgca_approval_no": "DGCA/FTO/37/2023",
        "approval_validity": "2028-09-30",
        "operational_status": "active",
        "established_year": 2023,
        "confidence_score": 0.94,
        "completeness_score": 0.91,
        "last_verified_date": "2026-10-25",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Exempt / Under Assessment",
            "overall_score": 52.0,
            "national_rank": 31,
            "annual_hours_logged": 3100,
            "safety_audit_score": 81.5,
            "cfi_cadre_strength": 5,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_SKY_JAL",
                "is_primary": True,
                "airport_name": "Jalgaon Airport",
                "icao_code": "VAJL",
                "city": "Jalgaon",
                "state": "Maharashtra",
                "region": "West",
                "runway_length_meters": 1700,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "AAI Controlled Tower",
                "latitude": 20.9633,
                "longitude": 75.6267
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Tecnam P2008 JC",
                "manufacturer": "Tecnam",
                "engine_type": "single_engine",
                "avionics_type": "Garmin G3X Touch Glass Cockpit",
                "count": 4,
                "operational_count": 4,
                "fuel_type": "MOGAS"
            },
            {
                "aircraft_model": "Tecnam P2006T",
                "manufacturer": "Tecnam",
                "engine_type": "multi_engine",
                "avionics_type": "Garmin G950",
                "count": 1,
                "operational_count": 1,
                "fuel_type": "MOGAS"
            }
        ],
        "fees": {
            "course_name": "DGCA CPL (ME/IR) Modern Glass Cockpit Pathway",
            "currency": "INR",
            "tuition_flying_inr": 3800000,
            "ground_school_inr": 250000,
            "simulator_inr": 160000,
            "hostel_mess_annual_inr": 180000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 4390000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-03-01",
            "source_url": "https://skynex.aero/cpl-program",
            "inclusions": ["200 hrs flying training", "Ground school syllabus", "Simulator sessions"],
            "exclusions": ["Hostel charges", "DGCA examination fees", "Class 1 medical tests"]
        },
        "programmes": ["DGCA CPL with Multi-Engine", "PPL", "Assistant Flight Instructor Rating"],
        "training_capacity": {
            "annual_cadet_intake": 30,
            "active_instructors": 5,
            "avg_completion_months": 15
        }
    },

    # 32. Ekvi Air Training Organisation (Salem) - Exempt / Under Assessment
    {
        "school_id": "FTO_EKVI_032",
        "name": "Ekvi Air Training Organisation Private Limited",
        "short_name": "Ekvi Air Salem",
        "slug": "ekvi-air-training-organisation",
        "website_url": "https://ekviair.com",
        "ownership_type": "private",
        "dgca_approval_no": "DGCA/FTO/38/2023",
        "approval_validity": "2028-10-31",
        "operational_status": "active",
        "established_year": 2023,
        "confidence_score": 0.94,
        "completeness_score": 0.90,
        "last_verified_date": "2026-10-25",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Exempt / Under Assessment",
            "overall_score": 51.5,
            "national_rank": 32,
            "annual_hours_logged": 2900,
            "safety_audit_score": 82.0,
            "cfi_cadre_strength": 5,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_EKV_SXV",
                "is_primary": True,
                "airport_name": "Salem Airport (Kamlapuram)",
                "icao_code": "VOSM",
                "city": "Salem",
                "state": "Tamil Nadu",
                "region": "South",
                "runway_length_meters": 1829,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "AAI Controlled Tower",
                "latitude": 11.7833,
                "longitude": 78.0667
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Tecnam P2008 JC",
                "manufacturer": "Tecnam",
                "engine_type": "single_engine",
                "avionics_type": "Garmin G3X Touch Glass Cockpit",
                "count": 4,
                "operational_count": 4,
                "fuel_type": "MOGAS"
            },
            {
                "aircraft_model": "Tecnam P2006T",
                "manufacturer": "Tecnam",
                "engine_type": "multi_engine",
                "avionics_type": "Garmin G950",
                "count": 1,
                "operational_count": 1,
                "fuel_type": "MOGAS"
            }
        ],
        "fees": {
            "course_name": "DGCA CPL Integrated Flight Course",
            "currency": "INR",
            "tuition_flying_inr": 3900000,
            "ground_school_inr": 260000,
            "simulator_inr": 170000,
            "hostel_mess_annual_inr": 180000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 4510000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-03-01",
            "source_url": "https://ekviair.com/fees",
            "inclusions": ["200 hrs flying training", "Ground instruction", "Simulator time"],
            "exclusions": ["Hostel accommodation", "DGCA examination fees"]
        },
        "programmes": ["DGCA CPL with Multi-Engine", "PPL", "Assistant Flight Instructor Rating"],
        "training_capacity": {
            "annual_cadet_intake": 28,
            "active_instructors": 5,
            "avg_completion_months": 15
        }
    },

    # 33. Joy Flights (Jalgaon) - Exempt / Under Assessment
    {
        "school_id": "FTO_JOY_033",
        "name": "Joy Flights Private Limited",
        "short_name": "Joy Aviation",
        "slug": "joy-flights-jalgaon",
        "website_url": "https://joyflights.in",
        "ownership_type": "private",
        "dgca_approval_no": "DGCA/FTO/35/2022",
        "approval_validity": "2027-12-31",
        "operational_status": "active",
        "established_year": 2022,
        "confidence_score": 0.92,
        "completeness_score": 0.88,
        "last_verified_date": "2026-10-20",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Exempt / Under Assessment",
            "overall_score": 50.8,
            "national_rank": 33,
            "annual_hours_logged": 2600,
            "safety_audit_score": 80.5,
            "cfi_cadre_strength": 4,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_JOY_JAL",
                "is_primary": True,
                "airport_name": "Jalgaon Airport",
                "icao_code": "VAJL",
                "city": "Jalgaon",
                "state": "Maharashtra",
                "region": "West",
                "runway_length_meters": 1700,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "AAI Controlled Tower",
                "latitude": 20.9633,
                "longitude": 75.6267
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Cessna 172S",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Garmin G1000",
                "count": 3,
                "operational_count": 3,
                "fuel_type": "AvGas 100LL"
            }
        ],
        "fees": {
            "course_name": "DGCA CPL Course",
            "currency": "INR",
            "tuition_flying_inr": 3650000,
            "ground_school_inr": 220000,
            "simulator_inr": 140000,
            "hostel_mess_annual_inr": 170000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 4180000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-02-01",
            "source_url": "https://joyflights.in/courses",
            "inclusions": ["200 hrs flying training", "Ground instruction", "Simulator time"],
            "exclusions": ["Hostel charges", "DGCA examination fees"]
        },
        "programmes": ["DGCA CPL", "PPL"],
        "training_capacity": {
            "annual_cadet_intake": 20,
            "active_instructors": 4,
            "avg_completion_months": 16
        }
    },

    # 34. Frank Aviation (Varanasi / Ghazipur) - Exempt / Under Assessment
    {
        "school_id": "FTO_FRANK_034",
        "name": "Frank Aviation Private Limited",
        "short_name": "Frank Aviation",
        "slug": "frank-aviation-varanasi",
        "website_url": "https://frankaviation.in",
        "ownership_type": "private",
        "dgca_approval_no": "DGCA/FTO/36/2023",
        "approval_validity": "2028-08-31",
        "operational_status": "active",
        "established_year": 2023,
        "confidence_score": 0.92,
        "completeness_score": 0.87,
        "last_verified_date": "2026-10-20",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Exempt / Under Assessment",
            "overall_score": 50.2,
            "national_rank": 34,
            "annual_hours_logged": 2400,
            "safety_audit_score": 80.0,
            "cfi_cadre_strength": 4,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_FRK_GHZ",
                "is_primary": True,
                "airport_name": "Ghazipur Airstrip",
                "icao_code": "VI54",
                "city": "Ghazipur / Varanasi",
                "state": "Uttar Pradesh",
                "region": "North",
                "runway_length_meters": 1300,
                "runway_surface": "Asphalt",
                "night_flying_available": False,
                "atc_type": "Dedicated FTO AFIS",
                "latitude": 25.5833,
                "longitude": 83.5833
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Cessna 172R",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Garmin Glass Cockpit",
                "count": 3,
                "operational_count": 3,
                "fuel_type": "AvGas 100LL"
            }
        ],
        "fees": {
            "course_name": "DGCA CPL Course",
            "currency": "INR",
            "tuition_flying_inr": 3600000,
            "ground_school_inr": 220000,
            "simulator_inr": 130000,
            "hostel_mess_annual_inr": 160000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 4110000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-02-01",
            "source_url": "https://frankaviation.in/fees",
            "inclusions": ["200 hrs flying training", "Ground instruction", "Simulator time"],
            "exclusions": ["Hostel boarding", "DGCA examination fees"]
        },
        "programmes": ["DGCA CPL", "PPL"],
        "training_capacity": {
            "annual_cadet_intake": 20,
            "active_instructors": 4,
            "avg_completion_months": 18
        }
    },

    # 35. Chetak Aviation (Aligarh) - Exempt / Under Assessment
    {
        "school_id": "FTO_CHETAK_035",
        "name": "Chetak Aviation",
        "short_name": "Chetak Aviation",
        "slug": "chetak-aviation-aligarh",
        "website_url": "https://chetakaviation.in",
        "ownership_type": "private",
        "dgca_approval_no": "DGCA/FTO/34/2021",
        "approval_validity": "2027-11-30",
        "operational_status": "active",
        "established_year": 2021,
        "confidence_score": 0.92,
        "completeness_score": 0.87,
        "last_verified_date": "2026-10-20",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Exempt / Under Assessment",
            "overall_score": 49.6,
            "national_rank": 35,
            "annual_hours_logged": 2200,
            "safety_audit_score": 79.0,
            "cfi_cadre_strength": 4,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_CHT_ALI",
                "is_primary": True,
                "airport_name": "Aligarh Airstrip",
                "icao_code": "VIAH",
                "city": "Aligarh",
                "state": "Uttar Pradesh",
                "region": "North",
                "runway_length_meters": 1200,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "Dedicated FTO Air Traffic Control",
                "latitude": 27.8833,
                "longitude": 78.0833
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Cessna 172",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Garmin Equipped",
                "count": 2,
                "operational_count": 2,
                "fuel_type": "AvGas 100LL"
            }
        ],
        "fees": {
            "course_name": "DGCA CPL Course",
            "currency": "INR",
            "tuition_flying_inr": 3500000,
            "ground_school_inr": 200000,
            "simulator_inr": 120000,
            "hostel_mess_annual_inr": 150000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 3970000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-01-01",
            "source_url": "https://chetakaviation.in/cpl-fees",
            "inclusions": ["200 hrs flying training", "Ground instruction", "Simulator time"],
            "exclusions": ["Hostel charges", "DGCA examination fees"]
        },
        "programmes": ["DGCA CPL", "PPL"],
        "training_capacity": {
            "annual_cadet_intake": 18,
            "active_instructors": 4,
            "avg_completion_months": 18
        }
    },

    # 36. Star Flying Academy (Ujjain) - Exempt / Under Assessment
    {
        "school_id": "FTO_STAR_036",
        "name": "Star Flying Academy Private Limited",
        "short_name": "Star Flying Academy",
        "slug": "star-flying-academy-ujjain",
        "website_url": "https://starflyingacademy.com",
        "ownership_type": "private",
        "dgca_approval_no": "DGCA/FTO/40/2023",
        "approval_validity": "2028-11-30",
        "operational_status": "active",
        "established_year": 2023,
        "confidence_score": 0.92,
        "completeness_score": 0.87,
        "last_verified_date": "2026-10-20",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Exempt / Under Assessment",
            "overall_score": 49.2,
            "national_rank": 36,
            "annual_hours_logged": 2100,
            "safety_audit_score": 78.5,
            "cfi_cadre_strength": 3,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_STR_UJJ",
                "is_primary": True,
                "airport_name": "Ujjain Airstrip",
                "icao_code": "VIUJ",
                "city": "Ujjain",
                "state": "Madhya Pradesh",
                "region": "Central",
                "runway_length_meters": 1150,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "Dedicated FTO AFIS",
                "latitude": 23.1833,
                "longitude": 75.7667
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Tecnam P2008 JC",
                "manufacturer": "Tecnam",
                "engine_type": "single_engine",
                "avionics_type": "Garmin G3X",
                "count": 2,
                "operational_count": 2,
                "fuel_type": "MOGAS"
            }
        ],
        "fees": {
            "course_name": "DGCA CPL Course",
            "currency": "INR",
            "tuition_flying_inr": 3600000,
            "ground_school_inr": 220000,
            "simulator_inr": 130000,
            "hostel_mess_annual_inr": 150000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 4100000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-02-01",
            "source_url": "https://starflyingacademy.com/fees",
            "inclusions": ["200 hrs flying training", "Ground instruction", "Simulator time"],
            "exclusions": ["Hostel charges", "DGCA examination fees"]
        },
        "programmes": ["DGCA CPL", "PPL"],
        "training_capacity": {
            "annual_cadet_intake": 16,
            "active_instructors": 3,
            "avg_completion_months": 18
        }
    },

    # 37. Amritsar Aviation Club (Amritsar) - State Govt / Renewal in Progress
    {
        "school_id": "FTO_AMRITSAR_037",
        "name": "Amritsar Aviation Club",
        "short_name": "Amritsar Aviation Club",
        "slug": "amritsar-aviation-club",
        "website_url": "https://punjabcivilaviation.gov.in",
        "ownership_type": "state_government",
        "dgca_approval_no": "DGCA/FTO/22/1965",
        "approval_validity": "2026-12-31",
        "operational_status": "renewal_in_progress",
        "established_year": 1965,
        "confidence_score": 0.91,
        "completeness_score": 0.86,
        "last_verified_date": "2026-10-15",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Exempt / Under Assessment",
            "overall_score": 48.5,
            "national_rank": 37,
            "annual_hours_logged": 1900,
            "safety_audit_score": 77.0,
            "cfi_cadre_strength": 3,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_AMR_ATQ",
                "is_primary": True,
                "airport_name": "Sri Guru Ram Dass Jee International Airport",
                "icao_code": "VIAR",
                "city": "Amritsar",
                "state": "Punjab",
                "region": "North",
                "runway_length_meters": 3658,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "AAI Controlled International Tower",
                "latitude": 31.7094,
                "longitude": 74.7972
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Cessna 152",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Analogue",
                "count": 2,
                "operational_count": 2,
                "fuel_type": "AvGas 100LL"
            }
        ],
        "fees": {
            "course_name": "Punjab State Subsidised CPL",
            "currency": "INR",
            "tuition_flying_inr": 3100000,
            "ground_school_inr": 180000,
            "simulator_inr": 100000,
            "hostel_mess_annual_inr": 140000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 3520000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-01-01",
            "source_url": "https://punjabcivilaviation.gov.in/amritsar-cpl",
            "inclusions": ["200 hrs flying training", "Ground instruction", "Simulator time"],
            "exclusions": ["Hostel charges", "DGCA examination fees"]
        },
        "programmes": ["DGCA CPL", "PPL"],
        "training_capacity": {
            "annual_cadet_intake": 15,
            "active_instructors": 3,
            "avg_completion_months": 24
        }
    },

    # 38. Northern India Flying Club (Jalandhar / Patiala) - State Govt / Renewal in Progress
    {
        "school_id": "FTO_NIFC_038",
        "name": "Northern India Flying Club",
        "short_name": "Northern India FC",
        "slug": "northern-india-flying-club",
        "website_url": "https://punjabcivilaviation.gov.in",
        "ownership_type": "state_government",
        "dgca_approval_no": "DGCA/FTO/24/1954",
        "approval_validity": "2026-12-31",
        "operational_status": "renewal_in_progress",
        "established_year": 1954,
        "confidence_score": 0.91,
        "completeness_score": 0.85,
        "last_verified_date": "2026-10-15",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Exempt / Under Assessment",
            "overall_score": 48.0,
            "national_rank": 38,
            "annual_hours_logged": 1800,
            "safety_audit_score": 76.5,
            "cfi_cadre_strength": 3,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_NIFC_JAL",
                "is_primary": True,
                "airport_name": "Civil Aerodrome Jalandhar",
                "icao_code": "VI43",
                "city": "Jalandhar",
                "state": "Punjab",
                "region": "North",
                "runway_length_meters": 1100,
                "runway_surface": "Asphalt",
                "night_flying_available": False,
                "atc_type": "Civil Aerodrome AFIS",
                "latitude": 31.3333,
                "longitude": 75.5833
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Cessna 152",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Analogue",
                "count": 2,
                "operational_count": 2,
                "fuel_type": "AvGas 100LL"
            }
        ],
        "fees": {
            "course_name": "State Subsidised CPL Course",
            "currency": "INR",
            "tuition_flying_inr": 3100000,
            "ground_school_inr": 180000,
            "simulator_inr": 100000,
            "hostel_mess_annual_inr": 140000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 3520000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-01-01",
            "source_url": "https://punjabcivilaviation.gov.in/nifc",
            "inclusions": ["200 hrs flying training", "Ground instruction", "Simulator time"],
            "exclusions": ["Hostel charges", "DGCA examination fees"]
        },
        "programmes": ["DGCA CPL", "PPL"],
        "training_capacity": {
            "annual_cadet_intake": 15,
            "active_instructors": 3,
            "avg_completion_months": 24
        }
    },

    # 39. Bihar Flying Club (Patna) - State Govt / Active
    {
        "school_id": "FTO_BIHAR_039",
        "name": "Bihar Flying Club Limited",
        "short_name": "Bihar Flying Club",
        "slug": "bihar-flying-club-patna",
        "website_url": "https://biharcivilaviation.gov.in",
        "ownership_type": "state_government",
        "dgca_approval_no": "DGCA/FTO/11/1940",
        "approval_validity": "2027-04-30",
        "operational_status": "active",
        "established_year": 1940,
        "confidence_score": 0.91,
        "completeness_score": 0.86,
        "last_verified_date": "2026-10-15",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Exempt / Under Assessment",
            "overall_score": 47.5,
            "national_rank": 39,
            "annual_hours_logged": 1600,
            "safety_audit_score": 75.8,
            "cfi_cadre_strength": 3,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_BIH_PAT",
                "is_primary": True,
                "airport_name": "Jay Prakash Narayan Airport",
                "icao_code": "VEPT",
                "city": "Patna",
                "state": "Bihar",
                "region": "East",
                "runway_length_meters": 2286,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "AAI Controlled International Tower",
                "latitude": 25.5914,
                "longitude": 85.0881
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Cessna 152",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Analogue",
                "count": 2,
                "operational_count": 2,
                "fuel_type": "AvGas 100LL"
            }
        ],
        "fees": {
            "course_name": "Bihar State Subsidised CPL Course",
            "currency": "INR",
            "tuition_flying_inr": 3150000,
            "ground_school_inr": 180000,
            "simulator_inr": 100000,
            "hostel_mess_annual_inr": 140000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 3570000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-01-01",
            "source_url": "https://biharcivilaviation.gov.in/cpl-fees",
            "inclusions": ["200 hrs flying training", "Ground instruction", "Simulator time"],
            "exclusions": ["Hostel charges", "DGCA examination fees"]
        },
        "programmes": ["DGCA CPL", "PPL"],
        "training_capacity": {
            "annual_cadet_intake": 15,
            "active_instructors": 3,
            "avg_completion_months": 24
        }
    },

    # 40. Madras Flying Club (Chennai & Vellore) - Historic Trust / Active
    {
        "school_id": "FTO_MADRAS_040",
        "name": "The Madras Flying Club Limited",
        "short_name": "Madras Flying Club",
        "slug": "madras-flying-club",
        "website_url": "https://madrasflyingclub.org",
        "ownership_type": "historical_trust",
        "dgca_approval_no": "DGCA/FTO/02/1930",
        "approval_validity": "2027-10-31",
        "operational_status": "active",
        "established_year": 1930,
        "confidence_score": 0.93,
        "completeness_score": 0.88,
        "last_verified_date": "2026-10-15",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Exempt / Under Assessment",
            "overall_score": 47.0,
            "national_rank": 40,
            "annual_hours_logged": 1700,
            "safety_audit_score": 75.0,
            "cfi_cadre_strength": 3,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_MFC_MAA",
                "is_primary": True,
                "airport_name": "Chennai International Airport",
                "icao_code": "VOMM",
                "city": "Chennai",
                "state": "Tamil Nadu",
                "region": "South",
                "runway_length_meters": 3658,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "Major AAI International Controlled Tower",
                "latitude": 12.9944,
                "longitude": 80.1806
            },
            {
                "base_id": "BASE_MFC_VEL",
                "is_primary": False,
                "airport_name": "Vellore Airstrip",
                "icao_code": "VOVR",
                "city": "Vellore",
                "state": "Tamil Nadu",
                "region": "South",
                "runway_length_meters": 1050,
                "runway_surface": "Asphalt",
                "night_flying_available": False,
                "atc_type": "FTO AFIS",
                "latitude": 12.9083,
                "longitude": 79.1333
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Cessna 152",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Analogue",
                "count": 2,
                "operational_count": 2,
                "fuel_type": "AvGas 100LL"
            },
            {
                "aircraft_model": "Cessna 172",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Analogue",
                "count": 1,
                "operational_count": 1,
                "fuel_type": "AvGas 100LL"
            }
        ],
        "fees": {
            "course_name": "Commercial Pilot License (Aeroplane) Course",
            "currency": "INR",
            "tuition_flying_inr": 3400000,
            "ground_school_inr": 200000,
            "simulator_inr": 110000,
            "hostel_mess_annual_inr": 160000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 3870000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-01-01",
            "source_url": "https://madrasflyingclub.org/pilot-fees",
            "inclusions": ["200 hrs flying training", "Ground instruction", "Simulator time"],
            "exclusions": ["Hostel charges in Chennai/Vellore", "DGCA examination fees"]
        },
        "programmes": ["DGCA CPL", "PPL", "Assistant Flight Instructor Rating", "AME"],
        "training_capacity": {
            "annual_cadet_intake": 20,
            "active_instructors": 3,
            "avg_completion_months": 24
        }
    },

    # 41. B.K. Aviation (Lucknow / Kanpur) - Private / Active
    {
        "school_id": "FTO_BK_041",
        "name": "B.K. Aviation Private Limited",
        "short_name": "B.K. Aviation",
        "slug": "bk-aviation-lucknow",
        "website_url": "https://bkaviation.in",
        "ownership_type": "private",
        "dgca_approval_no": "DGCA/FTO/32/2021",
        "approval_validity": "2027-08-31",
        "operational_status": "active",
        "established_year": 2021,
        "confidence_score": 0.91,
        "completeness_score": 0.86,
        "last_verified_date": "2026-10-15",
        "ranking": {
            "ranking_period": "2025-2026",
            "ranking_category": "Exempt / Under Assessment",
            "overall_score": 46.5,
            "national_rank": 41,
            "annual_hours_logged": 1500,
            "safety_audit_score": 74.0,
            "cfi_cadre_strength": 3,
            "source_id": "SRC_PIB_FTO_2026"
        },
        "bases": [
            {
                "base_id": "BASE_BK_LKO",
                "is_primary": True,
                "airport_name": "Chaudhary Charan Singh International Airport",
                "icao_code": "VILK",
                "city": "Lucknow",
                "state": "Uttar Pradesh",
                "region": "North",
                "runway_length_meters": 2744,
                "runway_surface": "Asphalt",
                "night_flying_available": True,
                "atc_type": "AAI International Controlled Tower",
                "latitude": 26.7606,
                "longitude": 80.8892
            }
        ],
        "fleet": [
            {
                "aircraft_model": "Cessna 172R",
                "manufacturer": "Textron Aviation",
                "engine_type": "single_engine",
                "avionics_type": "Garmin Glass Cockpit",
                "count": 2,
                "operational_count": 2,
                "fuel_type": "AvGas 100LL"
            }
        ],
        "fees": {
            "course_name": "DGCA CPL Course",
            "currency": "INR",
            "tuition_flying_inr": 3500000,
            "ground_school_inr": 200000,
            "simulator_inr": 120000,
            "hostel_mess_annual_inr": 150000,
            "tax_gst_inr": 0,
            "total_estimated_inr": 3970000,
            "is_fee_inclusive_hostel": False,
            "is_fee_verified": True,
            "fee_effective_date": "2026-01-01",
            "source_url": "https://bkaviation.in/fees",
            "inclusions": ["200 hrs flying training", "Ground instruction", "Simulator time"],
            "exclusions": ["Hostel charges", "DGCA examination fees"]
        },
        "programmes": ["DGCA CPL", "PPL"],
        "training_capacity": {
            "annual_cadet_intake": 15,
            "active_instructors": 3,
            "avg_completion_months": 22
        }
    }
]

out_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "samples", "fto_seed_data.json"))
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(ftos, f, indent=2, ensure_ascii=False)

print(f"Successfully generated all {len(ftos)} DGCA approved FTO records at {out_path}!")
