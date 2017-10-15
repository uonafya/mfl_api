# DHIS2 - KMHFL Integration v0.1

## DHIS2
- Not much needs to be done on this side. All you need to know is how to use the [dhis2 Web API v2.26](https://docs.dhis2.org/2.26/en/developer/html/dhis2_developer_manual_full.html#webapi "dhis2 Web API"). This will enable you to understand and maybe improve on the code that we shall see later im the MFL API section.
- You might also need **super user** credentials to __*dhis2*__ so that you can update the ones we have, if need be.
- Lastly, :smile:, If you decide to use the [dhis2 OAuth2 protocol](https://docs.dhis2.org/2.26/en/developer/html/dhis2_developer_manual_full.html#webapi_oauth2 "dhis2 OAuth2 Authentication Protocol") make sure you have created an **OAuth2 Client** in __*dhis2*__ and take note of the **Client ID** and **Client Secret**, you know, for the various *grant_types* to obtain your *OAuth2 Tokens*.

## MFL API
>### Disclaimer!
>- This doc/tutorial assumes that one has the knowledge to **correctly setup** and **run** the **MFL API**. Reference to [MFL API Docs](http://mfl-api-docs.readthedocs.io/en/latest/02_developer_install.html "MFL API Developer Installation") is advised, if need be.
- We might have a bit of work to do here :sweat_smile:. But no worries, we'll go step by step. I got your back :thumbsup:.

### I. Lets get the source code
- You should be in a python virtual environment through this whole tutorial. You can set it up real quick. Check out [virtualenv](https://virtualenv.pypa.io/en/stable/installation/ "Virtualenv Installation"). I also advise using python's [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/ "Virtualenvwrapper Installation") together with the virtual environment. It will save you a great deal.
- Hopefully, our git repository is still active; go to uonafya [mfl_api](https://github.com/uonafya/mfl_api "uonafya MFL API Git Repository") git repository and either download a zipped version of the repository or clone it over in the terminal via `:bash-$ git clone https://github.com/uonafya/mfl_api.git`.
- I believe everything went on as expected. You should now be having a folder called `mfl_api`, that's if you didn't provide an output folder name for `git clone`. Don't worry if the cloning takes a long time. The repository is around `167MB`.
- Next, check the branch that you are currently on. You can do this by `:bash-$ git branch`. You'll get an output such as:
```bash
bash-$ git branch
       develop
       mapping_models
     * master
       workforce17
```
Taking note of the `*`, we know that we are currently at branch `master`. We need to switch to `mapping-models`. To do so, run: `:bash-$ git checkout mapping-models`. You can `:bash-$ git branch` again just to confirm that the switching was successful. As a precautionary measure, kindly run: `:bash-$ git pull`. This makes sure you have all necessary resources in that branch.
- Now, we have the source code all set up.
#### NB* _The source code is already updated with the integration modules. We'll be going through the sections of the original code that was edited in oreder to effect the integration_.
- Ok, since we have that clarified, we can continue to the database setup.

### II. Setting up the database