# data science blog final

## blog post 1 -- 3/15/19

_What are the potential correlations between the demographics of public schools (income, race, dis/ability, ESL/ELL), and the resources/ opportunities available at those schools (edtech products, vocational/tech training programs, arts)?_

### Project introduction & overview

The most difficult component of this project so far has been deciding what kind of “stories” we might be able to tell with the data, based on not just what’s available, but also the common features between them; deciding on the “story” from even a preliminary scan of the data has been the general theme of our work for the past few weeks. 

We began by finding four of the most relevant datasets from government records, and splitting them up among our group members: school demographics (Amy), access to educational technology (Rebecca), career and technical education programs (Jessica), and arts education programs (YJ). Because these are all separate datasets, we thought that it would make sense to split them up “by person,” which would make the initial steps of understanding the basic information held within each dataset much easier. Furthermore, because all the datasets are set up/ formatted differently, this means that each of us should handle cleaning and preprocessing on our own datasets.

We’re combining information from a number of records/ studies/ surveys from the federal government, some of which are conducted by different agencies, which means that the schema are all formatted differently, and information types are often inconsistent (e.g. one survey will collect data on a per-school basis, and another will collect on a per-district basis). An additional difficulty in coming up with a coherent question or story is that many of these datasets are quite old and/or from different years, so patterns we find may not necessarily be accurate or relevant to the point in time that we’re trying to think about. That being said, an awareness of American history, geography, and resource distribution suggests that it’s unlikely that the content of these data changed drastically -- given that we don’t have additional resources available, we’re going to assume that this is the case but do so with the knowledge that we have incomplete information. 

The next two sections of the blog post will explain how we’re attempting to answer the question: what kinds of stories can we tell? What stories do we want to tell?

### Joinable Attributes

Given how disparate our datasets were, the first step was to find and decide on “joinable attributes” to link our datasets together. 

For each dataset, the most “relevant” attributes are listed below: 

* Demographics: state/location, school, enrollment
* Edtech: state/location, school region, race, community type, school enrollment size 
* CTE: region, community type (urban vs rural), district enrollment size
* Arts: school region (NE, SE, C, W), school community type (city, suburban, town, rural etc), school enrollment size, percent combined enrollment of black, hispanic, asian/pacific islander, or american indian/alaska native students in the school 

All of our datasets are national; region and enrollment are common among all datasets, but the detail and unit of region/enrollment are different. For instance, the dataset on Edtech divided the school enrollment size to these 3 categories: 1) less than 300 2) 300-999 3) 1000 or more, while the dataset on arts divided it to 1) less than 500 2) 500-999 3) 1000 or more. While we are able to easily combine the schools with 1000 or more students from both datasets to one, with the other two categories, things become more difficult. In this case, we can carefully make the assumption that schools with less than 500 students can encompass schools with less than 300 students and schools with 500-999 students is within the larger range of 300-999 students. We understand that making these generalizations can cause overlap in our data, especially when we set up our independent variables for further analysis (when building our linear regression model). We are open to all of your suggestions and will continue to explore new ways to combine and generalize our datasets.

Given this, our chosen “joins, ” ordered by priority, will be:
1. Location/region
2. Community type (rural/town/suburban/urban)
3. Enrollment

As noted above, enrollment is an important but especially finicky attribute. The example above indicates the difficulties in making approximations about enrollment types, but furthermore the units of evaluation are not constant across datasets (e.g. school vs district). To deal with this, one strategy we can apply is taking a percentile of both to provide an approximation for relative size. That being said, we’re not sure the extent to which enrollment would even be an explanatory variable -- absolute size of the district or school doesn’t necessarily indicate anything about the volume or distribution of resources within the school. If our results are too noisy after doing this, we may choose to remove enrollment. 

The rest of our analysis is predicated on the assumption that our chosen “joins” -- even when they don’t necessarily map to the same exact units or data points -- preserve most of the interesting information that we’re trying to extract, and entries from all four datasets where each of these attributes match will indicate information about very similar schools. We think that this is the case because though the data is represented differently, these are all nationwide surveys polling the same schools (or a random sample of those schools). 

That being said, we need to be careful about how exactly we do--or don’t--draw conclusions or correlations between these so-called “joinable attributes.” For instance, the arts education dataset and the CTE dataset have very joinable attributes, with two caveats: one, the arts dataset is school-wise, and the CTE dataset is districtwise; and two, the arts dataset also has a flag for the proportion of students of color. While we can make an approximation for which buckets to place each school or district into in terms of region and size, it doesn’t necessarily also make sense to draw a 1-1 mapping between matching region/size buckets and racial/ demographic information. 

Finally, we will pull in additional/ outside datasets that can link some attributes together. The US Census Bureau, for instance, has compiled the [Small Area Income and Poverty Estimates](https://www.census.gov/programs-surveys/saipe.html), which was used by the authors of the CTE survey (but frustratingly not included as a survey question!). Some preliminary calls to their API indicate that this dataset does contain some interesting information, in particular poverty levels for specific counties and school districts, which will not only allow us to create a baseline-level join for school-based data (which lists counties) and district-based data, but also provide an extra layer of explanatory information. 

### Features for analysis

Once we find a way to group the schools together, we will determine the best (most relevant features) among the datasets that best fit each classification method . For instance if the demographics or dis/ability of the classroom had a stronger correlation between certain metrics such as number of computers used, we would classify based on that feature.  Other classification methods such as linear regression can be used to determine whether a correlation exists between the relevant features and the dependent variables such as total time spent using computers. We will use the following classification models: 
Decision tree, linear regression, logistic regression, bayesian classification, SGD. 

The attributes that we’ll be looking at are:
* Enrollment demographics, particularly with breakdowns by AP enrollment and law enforcement referrals
* Computer usage by time & frequency
* Per-student computer access
* CTE program availability, and/or reasons for unavailability (the CTE dataset in particular has questions about whether financial need of schools or students play a role in the extent to which CTE programs are offered)
* Arts programs availability and participation rates

### Data cleaning, storage & representation

As noted above, each of us are cleaning our own datasets (since they have different shapes, number of attributes, etc.). That being said, we’re doing so in a standardized way, in particular, running python scripts to remove data with too many null values and then to organize the data. 

Our first, rough setup for data storage and representation is to dump everything into a SQL database, which will be useful and interesting for a high-level summary and overview of the relationship between different attributes we ant to look at. Each dataset will be a separate table, but we’re adding new columns in each table for processing the relevant joins as discussed above. 

As indicated in our pre-proposal, we hope our final product to have some sort of predictive component that encapsulates the relationships between different features. This means that we’ll want to create numeric schemata to translate qualitative attributes into something we can feed into statistical or numerical models. 

### Progress evaluation & next steps

By our next check-in after Spring Break, we will have finished constructing the SQL database, and created multiple visualizations of various complexities based on different queries to the database; furthermore, we should have sketched out some skeletons for what analytical models we’d like to use.

