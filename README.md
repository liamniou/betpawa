1. Build docker image and push it to your docker registry:
```
docker build . -t yourname/betpawa:1.0.0 && docker push yourname/betpawa:1.0.0
```

2. Update image name on 19th line of file manifests/deployment.yaml with actual image name that you've defined in previous step.

3. Create deployment, service and ingress in your cluster:
```
kubectl apply -f ./manifests
```

4. Point A record of your domain name (i.e. domainname.com, change it on 9th line of file manifests/ingress.yaml) to ClusterIP of your Kubernetes cluster.
