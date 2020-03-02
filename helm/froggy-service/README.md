### To install froggy-service as a new chart release:

Install production with release name `froggy-service-prod` in `default` namespace:
```
$ helm install -f values.prod.yaml --namespace default --name froggy-service-prod .
```

Install staging with release name `froggy-service-staging` in `staging` namespace:
```
$ helm install -f values.staging.yaml --namespace staging --name froggy-service-staging .
```

### To upgrade release by setting values:
```
$ helm upgrade -f values.prod.yaml --set backend.image.tag=$TAG --set frontend.image.tag=$TAG froggy-service-prod .
```

### To delete release, use `--purge` to make its name free:
```
$ helm delete froggy-service-prod
```

Further command and usage, see: [Helm](https://helm.sh/docs/)
