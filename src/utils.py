from verta import Client as ModelDBlient


def get_project_name() -> str:
    return "my-project"


def get_neuro_user() -> str:
    # TODO: replace this value with your Neu.ro username (`neuro config show | grep "User Name:"`)
    return "my-user"


def get_neuro_cluster() -> str:
    return "neuro-public"


def get_modeldb_client(experiment_name: str) -> "verta._tracking.experimentrun.ModelDBExperiment":
    modeldb_job = f"{get_project_name()}-modeldb-frontend"
    my_user = get_neuro_user()
    cluster = get_neuro_cluster()
    uri = f"http://{modeldb_job}--{my_user}.platform-jobs:3000"
    print(f"Connecting to ModelDB client {uri}")
    client = ModelDBlient(uri)
    exp = client.set_experiment(experiment_name)

    return client