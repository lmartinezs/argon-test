# argon-test
Is  a simple app that show you Hello World.

Have an endopoint to send a post request and return a counter of requests post method.

## GET: [environment].arkon.com/count/

## Result: 
post request:0

## POST: [environment].arkon.com/count/
post request: 1+

# Requeriments:
- git
- kubectl installed
- access to a kubernetes platform
- docker engine

# Test application

To test applicación in a kubernetes platform, you need download this repo.
and execute follow commands:

`git clone https://github.com/lmartinezs/argon-test.git`

`cd argo-test`

`kubectk apply -f kubernetes/`

Deployment will create 3 local environments.

| Environment | branch | Local domain |
| --- | --- | --- |
| Develop | develop | dev.arkon.com |
| Staging | staging | stg.arkon.com |
| Production | last release | prod.arkon.com |

Execute the following command to know address

`kubectl describe ingress | grep Address`
- Address:          192.168.49.2

Add the following lines to `/etc/hosts`:
- 192.168.49.2 stg.arkon.com
- 192.168.49.2 prod.arkon.com
- 192.168.49.2 dev.arkon.com

And then open stg.arkon.com domain on your browser

# CI/CD

## Add changes following gitflow method

Clone develop branch (default)
- `git clone https://github.com/lmartinezs/argon-test.git`

Create a feature/changes branch with: 
- `git checkout -b feature/new-changes`

Add you changes, commit and push new branch to repository
- `git add .`
- `git commit -m "test"`
- `git push --set-upstream origin feature/new-changes`

Pull request to merge feature/new-changes to develop using github platform

When you open a pull request, your code is tested with pylint

In PR merged to develop, githubActions... test, build and deploy to docker hub and kubernetes environment(Commented step)

In PR merged to staging, githubActions... test, build and deploy to docker hub and kubernetes environment(Commented step)

On create a new release, an action is executed to test, build and deploy to docker hub and prod environment(Commented step)





