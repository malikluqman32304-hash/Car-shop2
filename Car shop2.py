SQLite format 3   @                                                                     .ç˘   õ  ˆ…y
H	‹ß_‘õ                                                                                                                                                                                                                                                                                       Ç6))Ñ'tablecars_hatchbackcars_hatchbackCREATE TABLE cars_hatchback (
    hatchback_id INTEGER PRIMARY KEY,
    car_id INTEGER,
    engine TEXT,
    fuel_type TEXT,
    doors INTEGER,
    seats INTEGER,
    transmission TEXT,
    city_mileage INTEGER,
    FOREIGN KEY (car_id) REFERENCES cars_master(car_id)
)Ç?%%ÑAtablecars_classiccars_classicCREATE TABLE cars_classic (
    classic_id INTEGER PRIMARY KEY,
    car_id INTEGER,
    engine TEXT,
    condition TEXT,
    restoration_year INTEGER,
    originality TEXT,
    collector_value TEXT,
    showroom_status TEXT,
    FOREIGN KEY (car_id) REFERENCES cars_master(car_id)
)ÇF
%%ÑOtablecars_offroadcars_offroadCREATE TABLE cars_offroad (
    offroad_id INTEGER PRIMARY KEY,
    car_id INTEGER,
    engine TEXT,
    drivetrain TEXT,
    locking_differential TEXT,
    approach_angle INTEGER,
    departure_angle INTEGER,
    skid_plates TEXT,
    FOREIGN KEY (car_id) REFERENCES cars_master(car_id)
)ÇE	--Ñ=tablecars_convertiblecars_convertible
CREATE TABLE cars_convertible (
    convertible_id INTEGER PRIMARY KEY,
    car_id INTEGER,
    engine TEXT,
    roof_type TEXT,
    open_time INTEGER,
    wind_deflector TEXT,
    drive_type TEXT,
    summer_package TEXT,
    FOREIGN KEY (car_id) REFERENCES cars_master(car_id)
)Ç2Ñ7tablecars_vancars_van	CREATE TABLE cars_van (
    van_id INTEGER PRIMARY KEY,
    car_id INTEGER,
    engine TEXT,
    seating_capacity INTEGER,
    sliding_doors INTEGER,
    cargo_space INTEGER,
    fuel_type TEXT,
    family_package TEXT,
    FOREIGN KEY (car_id) REFERENCES cars_master(car_id)
)Ç/##Ñ%tablecars_sportscars_sportsCREATE TABLE cars_sports (
    sports_id INTEGER PRIMARY KEY,
    car_id INTEGER,
    engine TEXT,
    top_speed INTEGER,
    zero_to_sixty REAL,
    transmission TEXT,
    drive_type TEXT,
    track_mode TEXT,
    FOREIGN KEY (car_id) REFERENCES cars_master(car_id)
)Ç7##Ñ5tablecars_luxurycars_luxuryCREATE TABLE cars_luxury (
    luxury_id INTEGER PRIMARY KEY,
    car_id INTEGER,
    engine TEXT,
    interior TEXT,
    sound_system TEXT,
    climate_zones INTEGER,
    massage_seats TEXT,
    ambient_lighting TEXT,
    FOREIGN KEY (car_id) REFERENCES cars_master(car_id)
)Ç.!!Ñ'tablecars_truckcars_truckCREATE TABLE cars_truck (
    truck_id INTEGER PRIMARY KEY,
    car_id INTEGER,
    engine TEXT,
    payload INTEGER,
    towing_capacity INTEGER,
    bed_length INTEGER,
    axle_ratio REAL,
    fuel_type TEXT,
    FOREIGN KEY (car_id) REFERENCES cars_master(car_id)
)ÇM''ÑYtablecars_electriccars_electricCREATE TABLE cars_electric (
    electric_id INTEGER PRIMARY KEY,
    car_id INTEGER,
    battery_range INTEGER,
    charge_time INTEGER,
    motor_power INTEGER,
    fast_charge TEXT,
    warranty_years INTEGER,
    charging_type TEXT,
    FOREIGN KEY (car_id) REFERENCES cars_master(car_id)
)Ç*Ñ'tablecars_suvcars_suvCREATE TABLE cars_suv (
    suv_id INTEGER PRIMARY KEY,
    car_id INTEGER,
    engine TEXT,
    drivetrain TEXT,
    fuel_type TEXT,
    seats INTEGER,
    ground_clearance INTEGER,
    towing_capacity INTEGER,
    FOREIGN KEY (car_id) REFERENCES cars_master(car_id)
)Ç'!!Ñtablecars_sedancars_sedanCREATE TABLE cars_sedan (
    sedan_id INTEGER PRIMARY KEY,
    car_id INTEGER,
    engine TEXT,
    transmission TEXT,
    fuel_type TEXT,
    doors INTEGER,
    seats INTEGER,
    safety_rating INTEGER,
    FOREIGN KEY (car_id) REFERENCES cars_master(car_id)
)Å]##Établecars_mastercars_masterCREATE TABLE cars_master (
    car_id INTEGER PRIMARY KEY,
    brand TEXT,
    model TEXT,
    year INTEGER,
    category TEXT,
    base_price REAL,
    color TEXT,
    mileage INTEGER
)                                                                                                                                                                                                                                                                                          	 PetrolPetrolManual