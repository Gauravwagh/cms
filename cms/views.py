from django.shortcuts import render_to_response, render
from django.contrib.auth.decorators import login_required
from cms.models import Whatever
from cms.forms import UploadFileForm
from cms.models import Employee, Food, FoodAll
from django.core.context_processors import csrf
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect

import sys
import pandas as pd
import csv
import os
import dateutil.parser

@login_required
def upload_file(request):
	if request.method == "POST":
		file = request.FILES['file']
		# print request.FILES['file']
		file = os.path.join(os.path.dirname(__file__), 'employee.csv')

		# with open(file, 'rb') as csvfile:
		# 	spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
		# 	for row in spamreader:
		# 		try:
		# 			emp_min =  row[0].split(",")
		# 			emp_id = emp_min[0]
		# 			emp_name = emp_min[1]+" "+ row[1].split(",")[0]
		# 			emp_email = row[1].split(",")[1]
		# 			try:
		# 				employee = Employee.objects.get(employee_id=emp_id)
		# 			except:
		# 				employee = Employee(employee_id=emp_id, employee_name=emp_name, email=emp_email)
		# 				employee.save()
		# 		except:
		# 			pass

		emppp = Food.objects.all().delete()
		data = pd.read_csv(request.FILES['file'])  # you can also add params such as header, sep etc.
		array = data.values
		# print array
		datadict = []
		for i in array:
			col1 = i[0].split()
			# print i[0], "***"
			# print col1, "$$$$"
			hsw = col1[1].split("/")
			hsd = hsw[1]+"/"+hsw[1]+"/"+hsw[2]
			st_str = hsd + " " + col1[2]
			# print st_str, "=+================="
			hrs = col1[2].split(":")[0]
			if int(hrs)>17:
				type = "Dinner"
			else:
				type = "Lunch"
			dt = dateutil.parser.parse(st_str)
			# print dt
			# print dt
			try:
				emp = Employee.objects.get(employee_id=col1[0])
				try:
					food = Food.objects.get(employee=emp, type=type, avail_datetime=dt)
				except:
					food = Food(employee=emp, type=type, avail_datetime=dt)
					food.save()

				try:
					foodall = FoodAll.objects.get(employee=emp, type=type, avail_datetime=dt)
				except:
					food = FoodAll(employee=emp, type=type, avail_datetime=dt)
					food.save()
			except:
				pass
			ad = {}
			i = i[0].split(" ")
			ad[i[0]] = i[6], i[7]
			datadict.append(ad)




        #
		# merged = {}
		# for d in datadict:
		# 	for k, v in d.items():
		# 		if k not in merged: merged[k] = []
		# 		merged[k].append(v)
        #
		# # final = {}
		# # for k, v in merged.items ():
		# # 	final[k] = len(v)
        #
        #
        #
		# for k, v in merged.items():
		# 	merged[k].insert(0, len(v))
        #
		# # print merged
        #
		# myfile = open('finaldata.csv', 'wb')
		# wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
		# wr.writerow(["Employee ID", "No of Lunch/Dinner", "Lunch", "Dinner"])
		# for k, v in merged.items():
		# 	merged[k].insert(0, k)
		# 	smdata = []
		# 	for i in merged[k]:
		# 		if type(i) is tuple:
		# 			smdata.append(int(i[1].split(":")[0]))
		# 	if smdata:
		# 		lunch = sum(i < 17 for i in smdata)
		# 		dinner = sum(i > 17 for i in smdata)
		# 		merged[k].insert(2, lunch)
		# 		merged[k].insert(3, dinner)
		# 	wr.writerow(merged[k])


	form = UploadFileForm()
	return render(request, 'index.html',{"form":form})

def list(request):
	empdata = Employee.objects.all()
	form = UploadFileForm()
	if request.method == "POST":
		data = pd.read_csv(request.FILES['file'])  # you can also add params such as header, sep etc.
		array = data.values
		for one in array:
			try:
				emp = Employee.objects.get(employee_id=one[0])
			except:
				emp = Employee(employee_id=one[0], employee_name=one[1], email = one[2])
				emp.save()
	return render(request, 'cms/list.html',{"emp":empdata, "form":form})

def report(request):
	emp_id = Employee.objects.all()
	data = {}
	month = ""
	year = ""
	for emp in emp_id:
		emp_data = []
		emp_food = Food.objects.filter(employee=emp)
		# year = emp_food[0].avail_datetime.strftime('%Y')
		# print year, "&&&&&&&&&&&"
		lunch = 0
		dinner = 0
		total = 0
		for i in emp_food:
			month = i.avail_datetime.strftime('%B')
			year = i.avail_datetime.strftime('%Y')
			total = total + 1
			# print i.avail_datetime.strftime('%B'), i.avail_datetime, "-------"
			if i.avail_datetime.hour >= 5:
				lunch = lunch + 1
			else:
				dinner = dinner + 1
		# emp_data.append(emp)
		emp_data.append(lunch)
		emp_data.append(dinner)
		emp_data.append(total)
		data[emp] = emp_data
	date =  month + " "+ year
	return render(request, 'cms/report.html',{"month":month, "food":data, "date":date})


def export(request):
	emp_id = Employee.objects.all()
	data = {}
	month = ""
	for emp in emp_id:

		emp_data = []
		emp_food = Food.objects.filter(employee=emp)
		lunch = 0
		dinner = 0
		total = 0
		for i in emp_food:
			month = i.avail_datetime.strftime('%B')
			total = total + 1
			# print i.avail_datetime.strftime('%B'), i.avail_datetime, "-------"
			if i.avail_datetime.hour >= 5:
				lunch = lunch + 1
			else:
				dinner = dinner + 1
		# emp_data.append(emp)
		emp_data.append(lunch)
		emp_data.append(dinner)
		emp_data.append(total)
		data[emp] = emp_data

	# Create the HttpResponse object with the appropriate CSV header.
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

	writer = csv.writer(response)
	writer.writerow(['Employee ID', 'Name', 'Lunch', 'Dinner', 'Total'])
	for key in data:
		writer.writerow([key.employee_id, key.employee_name, data[key][0], data[key][1], data[key][2]])

	return response
