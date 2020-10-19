from src.utils import get_modeldb_client


def test_modeldb():
    # See official example: 
    # https://github.com/VertaAI/modeldb?ref=hackernoon.com#up-and-running-in-5-minutes

    client = get_modeldb_client(experiment_name="Test Experiment")
    run = client.set_experiment_run("Test Run")

    run.log_hyperparameters({"regularization" : 0.5})
    # ... model training code goes here
    run.log_metric('accuracy', 0.72)

    # log the second run
    run = client.set_experiment_run("Second Run")
    run.log_hyperparameters({"regularization" : 0.8})
    # ... model training code goes here
    run.log_metric('accuracy', 0.83)
