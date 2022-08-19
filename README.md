# Finite State Controller assisted Safe Planning

## Steps to setup:
- Clone the repository
- Use python3.7
- Install the required python libraries:
    - gekko==1.0.2
    - numpy==1.20.0

## Steps to learn the FSC
- Enter the directory for the experiment setup you want to run (Eg: cd Toy\ Problem/)
- Run the EM algorithm: python3.7 EM.py data_set/data_file_used no_of_states (python3.7 EM.py data_set/Toy_train_data 2)
    - Runs and stores 10 runs of FSC learning. Stored in results folder.
- Run test to find the best run:  python3.7 test.py data_set/data_file_used no_of_states (Eg: python3.7 test.py data_set/Toy_train_data 2) (For Toy Problem 4x2 run: python3.7 test2.py data_set/Toy_train_data_2_4 2)
    - Chooses the best run out of the 10 runs based on accuracy

## Steps to learn the planning agent
- Learn and store policy in the policy folder.
- Toy Problem
    - 4x1
        - python3.7 FSA_Agent_combVar.py height width rug_height rug_width starting_y_location_rug starting_x_location_rug end_location_y end_location_x generated_policy_name gekko_solver_number nse_limit nse_limit data_set/data_file_used no_of_states
        - Eg: python3.7 FSA_Agent_combVar.py 1 4 1 1 0 2 0 3 1_4 1 0 0 data_set/Toy_train_data 2
    - 4x2
        - python3.7 FSA_Agent_combVar2.py height width rug_height rug_width starting_y_location_rug starting_x_location_rug end_location_y end_location_x generated_policy_name gekko_solver_number nse_limit nse_limit data_set/data_file_used no_of_states
        - Eg: python3.7 FSA_Agent_combVar2.py 2 4 1 1 0 2 0 3 2_4 1 0 0 data_set/Toy_train_data_2_4 2
- Box Pushing/Markovian Boxpushing
    -  python3.7 FSA_Agent_combVar.py grid_size rug_height rug_width starting_y_location_rug starting_x_location_rug end_location_y end_location_x generated_policy_name gekko_solver_number nse_limit_severe nse_limit_mild data_set/data_file_used no_of_states slack
    - python3.7 FSA_Agent_combVar.py 15 7 3 6 4 7 14 15_15_pol 1 0 0 data_set/BP_15_15_35_25 6 20
- Navigation/Markovian Navigation
    - python3.7 FSA_Agent_combVar.py grid_size end_location_y end_location_x data_set/data_file_used no_of_states slack nse_limit_severe nse_limit_mild generated_policy_name
    - python3.7 FSA_Agent_combVar.py 15 14 14 data/Nav_15_15_30_30 2 15 0 0 Nav_pol_300_2_15_1_1