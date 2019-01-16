# HEPPA
HEPPA: hyvin edistynyt perjantaipiirretty applikaatio.
Web-app that allows approval voting (with veto), intended for selecting the Gurula friday cartoon. Started as a database application project over winter break 2018-2019.

[App on Heroku](http://heppa.herokuapp.com/)

## Installation Instructions
### Local Setup
Run these in the root directory to launch the app at 
```
> python3 -m venv venv
> source venv/bin/activate
> pip install -r requirements.txt
> python3 run.py
```

You can then open the app in your browser at `http://127.0.0.1:5000/`

### Heroku Setup
Simply make sure the application name in the command below is unique
```
heroku create example-heppa
```

You should then be able to open the app in `<example-heppa>.herokuapp.com`

If you've forked this on GitHub, you may want to use [Heroku's GitHub integration](https://devcenter.heroku.com/articles/github-integration).

## User Instructions

**NB: this application is not secure in any way. Do not reuse passwords or otherwise expect that anything you enter into this application is stored securely**

Before voting, you need to register an account. It is recommended that you use an empty password for maximum security.

After registering, you can add candidates and vote on them. The electoral system is [approval voting](https://en.wikipedia.org/wiki/Approval_voting) with the addition of an unrestricted veto right for everyone. Voting is not anonymous so that the veto cannot be abused.
