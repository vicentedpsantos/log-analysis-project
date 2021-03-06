<h1>Log Analysis Project</h1>

This project aims to analyze data coming from a pre-set database. The goals were to identify the most popular articles and authors, as well as pinpoint the day where most of the HTTP request errors happened within a given date range.

<h2>Prerequisites: </h2>
	python 2.7  
	Vagrant  
	VirtualBox  

<h2>Installation of prerequisites:</h2>
	
1. Install Vagrant and VirtualBox
2. Clone Udacity's Repo at [Udacity](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip "Udacity Fullstack-Nanodegree-VM")
3. Download the database from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip "database") 
4. Download the file log-analysis-project.py from this repository
4. Place all files within the vagrant folder of the repo you've just cloned. fullstack-nanodegree-vm > vagrant > new folder (log-analysis)

5. For the python download, go to:  
⋅⋅* **On Windows**, go to https://www.python.org/downloads/windows/  
⋅⋅* **On Linux**, on the terminal run command sudo apt install python2.7 python-pip  
⋅⋅* **On MacOS**, go to https://www.python.org/downloads/mac-osx/  

<h2>To run this project:</h2>
	
	Open your terminal/command prompt cd into fullstack-nanodegree-vm > vagrant
	Make sure file named Vagrantfile is in the folder by using the command ls
	run vagrant with the command vagrant up
	run vagrant ssh
	cd into folder /vagrant/log-analysis
	
**Creating necessary views**: 
1. run psql -d news
2. run `create view totalrequests as select count(*) as total, date(TIME) as date from log group by date;`
3. run `create view errorrequests as select count(*) as total, date(TIME) as date from log where status != '200 OK' group by date;`
4. run `create view requests_and_errors as select sum(errorrequests.total) as total_errors, sum(totalrequests.total) as total_requests, errorrequests.date from errorrequests, totalrequests where errorrequests.date = totalrequests.date group by errorrequests.date;` 

	Press ctrl + D to exit PSQL  
	Run python log-analysis-project.py  

<h2>Built With</h2>
	Vagrant, VirtualBox  
	PostgreSQL, python  

