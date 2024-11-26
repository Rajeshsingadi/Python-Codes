students_marks.csv			
			
student_id	name	subject	marks
1	Alice	Math	85
1	Alice	Science	90
2	Bob	Math	78
2	Bob	Science	88
3	Charlie	Math	92
3	Charlie	Science	95


students_details.csv	
	
student_id	age	gender
1	20	F
2	21	M
3	22	M

Expected output					
student_id	name	Math	Science	age	gender
1			Alice	85		90	20	F
2			Bob		78		88	21	M
3			Charlie	92		95	22	M


spark = SparkSession.builder.appName("StudentMarksList").getOrCreate()

student_marks = spark.read.csv("/path/to/file/students_marks.csv", header=True)

student_details = spark.read.csv("/path/to/file/students_details.csv" , header=True)

student_marks = student_marks.groupBy("student_id", "name" )

combined_data = student_marks.join(student_details, on="student_id", how="inner")
final_data = combined_data.groupBy("student_id", "name" )




Products

Product_Id, Product_Name, Unit_Price


Stores
Store_Id, Store_Name

Transaction (3 years of data)

Id Transaction_date Store_Id Product_Id Qty_Sold

O/p

Transaction_Month Store_Name Product_name total_Qty_Sold


each transction month wise and each store wise and one best selling product
yyyy-mm

with BestTransacion as (
select Dateformat(t.Transaction_date, 'yyyy-mm' ) as Transaction_Month ,Store_Name ,
 Product_name,
 row_number() over parition by(t.Transaction_date, "yyyy-mm",Store_name order by SUM(t.Qty_Sold) as total_Qty_Sold desc) as rnk from 
Products p join 
Transaction t on p.Product_Id=t.Product_Id join
Stores s on s.Store_Id=t.Store_Id
group by 
t.Transaction_Month, s.Store_Name, p.Product_name
)

select Transaction_Month, ,Store_Name ,Product_name, total_Qty_Sold from 
BestTransacion 
where 
rnk=1
