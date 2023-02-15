--Q2.1
SELECT D.id, D.department, COUNT(I.patient_id) as 'NoofIns' FROM doctors_info1 D
JOIN inspections2 I ON D.id = I.doctor_id
GROUP By D.id;

--Q2.2
SELECT strftime('%d', I.inspection_date) AS 'DayOfMonth', COUNT(I.patient_id) As 'NoofIns' from inspections2 I
GROUP by DayOfMonth
ORDER by NoofIns DESC;

--Q2.3
SELECT i1.inspection_date,  
		(count(i1.inspection_date)-COUNT(i2.inspection_date)) over()
From inspections2 as i1, inspections2 as i2
WHERE DATE(i2.inspection_date) = DATE(i1.inspection_date, '-1 days')
GROUP by i1.inspection_date
LIMIT 20

SELECT STRFTIME(i.inspection_date), DATE(i.inspection_date, '1 days')  from inspections2 i 


--Q2.4
SELECT d.deparment, CASE p.patient_id


