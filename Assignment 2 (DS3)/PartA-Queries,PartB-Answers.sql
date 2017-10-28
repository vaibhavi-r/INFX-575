--------------------------------------------
--PART A : SPARK SQL QUERIES
--------------------------------------------
--Schema: subject  predicate  object  [context]

-- Question 1
SELECT COUNT(*) as num_rows
FROM fbFacts
/*
num_rows
563,980,447
*/

-- Question 2
SELECT COUNT(DISTINCT predicate) as num_predicates
FROM fbFacts
/*
num_predicates
18,944
*/

-- Question 3
SELECT *
FROM fbFacts
WHERE subject = '/m/0284r5q'
/*
subject		predicate					obj						context
/m/0284r5q	/type/object/key			/wikipedia/en_id		9,327,603
/m/0284r5q	/type/object/key			/wikipedia/en			Flyte_$0028chocolate_bar$0029
/m/0284r5q	/type/object/key			/wikipedia/en_title		Flyte_$0028chocolate_bar$0029
/m/0284r5q	/common/topic/article		/m/0284r5t	
/m/0284r5q	/type/object/type			/common/topic	
/m/0284r5q	/type/object/type			/food/candy_bar	
/m/0284r5q	/type/object/type			/business/brand	
/m/0284r5q	/type/object/type			/base/tagit/concept	
/m/0284r5q	/food/candy_bar/manufacturer  /m/01kh5q	
/m/0284r5q	/common/topic/notable_types	  /business/brand	
/m/0284r5q	/common/topic/notable_types	  /food/candy_bar	
/m/0284r5q	/food/candy_bar/sold_in		/m/09c7w0	
/m/0284r5q	/common/topic/notable_for	{"types":[], "id":"/food/candy_bar", "property":"/type/object/type", "name":"Candy bar"}
/m/0284r5q	/type/object/name			/lang/en				Flyte
/m/0284r5q	/common/topic/image			/m/04v6jtv
*/

-- Question 4
SELECT COUNT(distinct subject) as num_travel_destinations
FROM fbFacts
WHERE predicate = '/type/object/type' AND
obj ='/travel/travel_destination'
/*
num_travel_destinations
295
*/

-- Question 5
--Find name of the tourist cities
SELECT f2.context as destination_name, count(f3.subject) as num_attractions
FROM fbFacts f1, fbFacts f2, fbFacts f3
WHERE  
f1.predicate = '/type/object/type' AND
f1.obj ='/travel/travel_destination' AND
f1.subject = f2.subject AND
f2.predicate = '/type/object/name' AND
f2.obj ='/lang/en' AND
f2.subject = f3.subject AND
f3.predicate ='/travel/travel_destination/tourist_attractions'  
GROUP BY f1.subject, f2.context
ORDER BY count(f3.subject) DESC, f2.context ASC
LIMIT 20

/*
destination_name	num_attractions
London	            108
Norway	            74
Finland	            59
Burlington	        41
Rome	            40
Toronto				36
Beijing				32
Buenos Aires		28
San Francisco		26
Bangkok				20
Munich				19
Sierra Leone		19
Vienna				19
Montpelier			18
Athens				17
Atlanta				17
Tanzania			17
Berlin				16
Laos				16
Portland			15
*/

-- Question 6
SELECT X.num_predicates as num_predicates, count(X.num_predicates) as frequency
FROM (SELECT COUNT(DISTINCT predicate) as num_predicates
		FROM fbFacts
		GROUP BY subject) X
GROUP BY X.num_predicates
/*

For image, refer partA-Q6-histogram.png
*/

--------------------------------------------
--PART B : MULTIPLE CHOICE
--------------------------------------------

/*
1. For Spark to use local files instead of HDFS, what additional preprocessing step is needed before even opening my Zeppelin notebook to prepare the data?
Answer 1: C (Replicate the data to be on all the nodes in the cluster.)
Reason: All slaves need a copy of the local data, unless data is in distributed file system like HDFS

2. How is Spark different from Hadoop MapReduce?
Answer 2: B (Spark writes intermediate results to memory while Hadoop writes to disk.)

3. Which of the following is NOT a good use case of MapReduce? 
Answer 3: B (Running a large number of transactions for a major bank.)
Reason: Transaction Processing is not possible, and has limited support in MapReduce paradigm.

4. In a simple MapReduce job with m mapper tasks and r reducer tasks, how many output files do you get?
Answer 4: C (r)
Reason: Number of output files should equal number of reducers.

5. One of the key features of Map-Reduce and Spark is their ability to cope with server failure. For each statement below indicate whether it is true or false.
A) In MapReduce, every map task and every reduce task is replicated across several workers.
B) When a server fails, Spark recomputes the RDD partitions at that server from parent RDD partitions.
C) In Spark, when the programmer calls the persist() function, the data is stored on disk, to facilitate recovery from failure.
D) When a server running a reduce task fails, MapReduce restarts that reduce task either at the same or another server, reusing data stored in local files at the mappers.

Answer 5 & Reasons:
A) FALSE
B) TRUE. Persisting intermediate results using RDDs is a big benefit of using Spark.
C) FALSE. Spark provides multiple storage levels such as MEMORY_ONLY, MEMORY_AND_DISK etc as options for persist()
D) TRUE. 
*/

--------------------------------------------
--THE END
--------------------------------------------
