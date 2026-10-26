# Fabric workspace migration POC

This repository contains a small set of Microsoft Fabric artifacts and a GitHub
Actions check to explore source control and CI/CD.

## Sample artifacts

- [`HelloWorld.Notebook`](./HelloWorld.Notebook/) - a PySpark notebook that
  creates and displays a tiny in-memory DataFrame.
- [`HelloWorld.DataPipeline`](./HelloWorld.DataPipeline/) - a Data Factory
  pipeline with one five-second Wait activity.
- [`.github/workflows/test.yml`](./.github/workflows/test.yml) - validates the
  sample definitions on pushes and pull requests. It does not connect to or
  deploy to a Fabric workspace.

The Notebook and Data Pipeline folders use Fabric Git integration's item
folder convention. Use the **Source control** pane in a Fabric workspace to
connect the repository and branch, then update the workspace from Git. Fabric
support and definition requirements can change; validate these starter
definitions in a disposable workspace before using them as a deployment
baseline.

## Authentication options to investigate

Keep the two authentication boundaries separate:

1. **Fabric workspace to Git provider:** when a workspace is connected to
   GitHub, Fabric needs Git-provider credentials/authorization to read and
   write the repository. User sign-in is the simplest POC. GitHub repository
   permissions and Fabric workspace permissions both apply.
2. **Automation to Fabric APIs:** for API calls from a CI runner, acquire a
   Microsoft Entra token for `https://api.fabric.microsoft.com`. Delegated
   user sign-in is convenient for local experiments. For unattended runs,
   evaluate a service principal and workload identity federation (OIDC) rather
   than committing credentials. A service principal must be allowed by the
   Fabric tenant settings and granted the required workspace permissions.

The identity used by a GitHub Actions job to call Fabric APIs is not
automatically the same as the Git credentials configured for the Fabric
workspace. Do not add client secrets, access tokens, or personal access tokens
to this repository. Store any required credentials in a secure identity
provider or protected GitHub environment secrets.

## Deployment options

- **Fabric Git integration:** update a workspace from its connected branch, or
  commit workspace changes back to Git. This is source control and workspace
  synchronization; it does not by itself promote content through environments.
- **Fabric deployment pipelines:** promote supported items between Fabric
  stages such as Development, Test, and Production. This is the built-in
  environment-promotion experience.
- **Fabric REST APIs from GitHub Actions:** automate Git synchronization or
  item definition import/export when the relevant API supports the item and
  operation. Handle asynchronous operations and environment-specific
  configuration explicitly.

## GitHub Actions vs. Fabric Git integration

| Capability | Fabric Git integration | GitHub Actions |
| --- | --- | --- |
| Main purpose | Keep a Fabric workspace and a Git branch in sync | Run automated jobs in response to GitHub events or manual dispatch |
| Where it runs | Inside the Fabric service | On a GitHub-hosted or self-hosted runner |
| Typical work | Compare, commit, and update Fabric item definitions | Validate files, run tests, call APIs, or orchestrate deployment |
| What this POC does | Provides sample Fabric item folders for a workspace to sync | Checks the sample definitions; it does not deploy them |

They complement each other: a developer can commit workspace changes to Git,
then a GitHub Actions workflow can validate the commit and, after authentication
and deployment steps are deliberately configured, orchestrate further
automation.

## Suggested POC sequence

1. Connect a disposable Fabric workspace to this GitHub repository and branch.
2. Update the workspace from Git and inspect the sample Notebook and Data
   Pipeline. Run the Notebook and pipeline manually.
3. Make a small change in the workspace, review the Git diff, and commit it.
4. Open a pull request and observe the validation job in GitHub Actions.
5. Compare branch-based workspace synchronization with a Fabric deployment
   pipeline. Only after that, prototype API deployment from a protected
   workflow/environment.

## Microsoft Learn references

- [Fabric Git integration overview](https://learn.microsoft.com/fabric/cicd/git-integration/intro-to-git-integration)
- [Fabric Git integration process and permissions](https://learn.microsoft.com/fabric/cicd/git-integration/git-integration-process)
- [Automate Fabric Git integration with APIs](https://learn.microsoft.com/fabric/cicd/git-integration/git-automation)
- [Fabric deployment pipelines overview](https://learn.microsoft.com/fabric/cicd/deployment-pipelines/intro-to-deployment-pipelines)
- [Fabric API quickstart and Entra tokens](https://learn.microsoft.com/rest/api/fabric/articles/get-started/fabric-api-quickstart)
