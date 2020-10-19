# MLOps Recipe: ModelDB
Sample configuration of [ModelDB system](https://docs.verta.ai/en/master/overview/modeldb.html) for model versioning, metadata, and experiment management.

# Quick setup on Neu.ro platform

1. Install and configure [Neu.ro client](https://github.com/neuromation/platform-client-python):
```bash
make init
```

2. Run ModelDB services:
```bash
make modeldb-up
```

3. Replace placeholder `my-user` with your actual username on Neu.ro platform in function `get_neuro_user()` in file [src/utils.py](src/utils.py):
```bash
neuro config show | grep 'User Name:'
```

4. Run a sample job that uses ModelDB client:
```bash
make modeldb-example
```

5. Shut down ModelDB services:
```bash
make modeldb-down
```
