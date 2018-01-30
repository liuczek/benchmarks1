from django.shortcuts import render
from .models import Result
from attributes.models import Attributes, Options, Labels
from django_filters import FilterSet, CharFilter, NumberFilter
import time
from statistics import mean, stdev
from collections import Counter
from math import sqrt
from scipy.stats import norm

def quartal_months(month_in_question):
	if month_in_question%3==1: 	return [month_in_question+1,month_in_question+2,month_in_question]
	if month_in_question%3==2: 	return [month_in_question+1,month_in_question-1,month_in_question]
	if month_in_question%3==0: 	return [month_in_question-1,month_in_question-2,month_in_question]	

def boxes(freq_one,values):
	box=0
	for i in values:
		box=box+freq_one[i]
	return box

def colnum_string(n):
    string = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        string = chr(65 + remainder) + string
    return string

def sign (a,b,c,d):
		count_1=column_count[a]
		count_2=column_count[b]
		abs_1=c*count_1
		abs_2=d*count_2
		#print (((abs_2*count_1/count_2)*(1-abs_2/count_2)*(1-count_1/count_2)))			
		if count_2>0: square=((abs_2*count_1/count_2)*(1-abs_2/count_2)*(1-count_1/count_2))
		if count_2==0: square=0
		if square>=0: divider=sqrt(square)
		if square<0: divider=0		
		if divider>0: chi_kvadrat=(abs_1-(abs_2*count_1/count_2))/divider
		if divider==0: chi_kvadrat=0			
		if chi_kvadrat<chi_sig_9995*-1 and b==0: 
			results_fin[len(results_fin)-1]['sig_total_9995_minus']=1
		elif chi_kvadrat<chi_sig_995*-1 and b==0: 
			results_fin[len(results_fin)-1]['sig_total_995_minus']=1
		elif chi_kvadrat<chi_sig_975*-1 and b==0: 
			results_fin[len(results_fin)-1]['sig_total_975_minus']=1
		elif chi_kvadrat>chi_sig_9995 and b==0: 
			results_fin[len(results_fin)-1]['sig_total_9995_plus']=1
		elif chi_kvadrat>chi_sig_995 and b==0: 
			results_fin[len(results_fin)-1]['sig_total_995_plus']=1
		elif chi_kvadrat>chi_sig_975 and b==0: 			
			results_fin[len(results_fin)-1]['sig_total_975_plus']=1			
		if a-b==1 and attribute_selected==999:					
			if chi_kvadrat>chi_sig_9995 and b>0 and 'sig_9995_plus' not in (results_fin[len(results_fin)-1].keys()):  
				results_fin[len(results_fin)-1]['sig_9995_plus']="#8593"
			elif chi_kvadrat>chi_sig_995 and b>0 and 'sig_995_plus' not in (results_fin[len(results_fin)-1].keys()):  
				results_fin[len(results_fin)-1]['sig_995_plus']="#8593"
			elif chi_kvadrat>chi_sig_975 and b>0 and 'sig_975_plus' not in (results_fin[len(results_fin)-1].keys()):  
				results_fin[len(results_fin)-1]['sig_975_plus']="#8593"		
			elif chi_kvadrat<chi_sig_9995*-1 and b>0 and 'sig_9995_plus' not in (results_fin[len(results_fin)-1].keys()):  
				results_fin[len(results_fin)-1]['sig_9995_plus']="#8595"
			elif chi_kvadrat<chi_sig_995*-1 and b>0 and 'sig_995_plus' not in (results_fin[len(results_fin)-1].keys()):  
				results_fin[len(results_fin)-1]['sig_995_plus']="#8595"
			elif chi_kvadrat<chi_sig_975*-1 and b>0 and 'sig_975_plus' not in (results_fin[len(results_fin)-1].keys()):  
				results_fin[len(results_fin)-1]['sig_975_plus']="#8595"						
			elif chi_kvadrat>chi_sig_9995 and b>0 and 'sig_9995_plus' in (results_fin[len(results_fin)-1].keys()):  
				results_fin[len(results_fin)-1]['sig_9995_plus']=results_fin[len(results_fin)-1]['sig_9995_plus']+colnum_string(b)
			elif chi_kvadrat>chi_sig_995 and b>0 and 'sig_995_plus' in (results_fin[len(results_fin)-1].keys()):  
				results_fin[len(results_fin)-1]['sig_995_plus']=results_fin[len(results_fin)-1]['sig_995_plus']+colnum_string(b)
			elif chi_kvadrat>chi_sig_975 and b>0 and 'sig_975_plus' in (results_fin[len(results_fin)-1].keys()):  
				results_fin[len(results_fin)-1]['sig_975_plus']=results_fin[len(results_fin)-1]['sig_975_plus']+colnum_string(b)	
		if attribute_selected!=999:		
			if chi_kvadrat>chi_sig_9995 and b>0 and 'sig_9995_plus' not in (results_fin[len(results_fin)-1].keys()):  
				results_fin[len(results_fin)-1]['sig_9995_plus']=colnum_string(b)
			elif chi_kvadrat>chi_sig_995 and b>0 and 'sig_995_plus' not in (results_fin[len(results_fin)-1].keys()):  
				results_fin[len(results_fin)-1]['sig_995_plus']=colnum_string(b)
			elif chi_kvadrat>chi_sig_975 and b>0 and 'sig_975_plus' not in (results_fin[len(results_fin)-1].keys()):  
				results_fin[len(results_fin)-1]['sig_975_plus']=colnum_string(b)			
			elif chi_kvadrat>chi_sig_9995 and b>0 and 'sig_9995_plus' in (results_fin[len(results_fin)-1].keys()):  
				results_fin[len(results_fin)-1]['sig_9995_plus']=results_fin[len(results_fin)-1]['sig_9995_plus']+colnum_string(b)
			elif chi_kvadrat>chi_sig_995 and b>0 and 'sig_995_plus' in (results_fin[len(results_fin)-1].keys()):  
				results_fin[len(results_fin)-1]['sig_995_plus']=results_fin[len(results_fin)-1]['sig_995_plus']+colnum_string(b)
			elif chi_kvadrat>chi_sig_975 and b>0 and 'sig_975_plus' in (results_fin[len(results_fin)-1].keys()):  
				results_fin[len(results_fin)-1]['sig_975_plus']=results_fin[len(results_fin)-1]['sig_975_plus']+colnum_string(b)					

def test(request):
	global column	
	global chi_sig_9995, chi_sig_995, chi_sig_975
	global column_num	
	global results_fin
	global column_count
	global attribute_selected
	sig_total=False
	sig_paired=False
	filtry=[]
	if request.GET.get("filtr_1")!=None and int(request.GET.get("filtr_1"))>0: filtry.append(request.GET.get("filtr_1"))
	if request.GET.get("filtr_2")!=None and int(request.GET.get("filtr_2"))>0: filtry.append(request.GET.get("filtr_2"))
	if request.GET.get("filtr_3")!=None and int(request.GET.get("filtr_3"))>0: filtry.append(request.GET.get("filtr_3"))	
	if request.GET.get("sig_total")=="true": sig_total=True
	if request.GET.get("sig_paired")=="true": sig_paired=True
	question = 1
	start_time = time.time()
	all_options=sorted(list((Result.objects.filter().values_list('parametres__Option_Code',flat=True).distinct())))
	all_options_fin=(Options.objects.filter(Option_Code__in=all_options))
	#if len(filtry)==0: data_filtered=(Result.objects.filter())
	if len(filtry)==0: id_filtered=(Result.objects.filter().values_list("answer_id",flat=True))	
	if len(filtry)==1: id_filtered=(Result.objects.filter(parametres__Option_Code=filtry[0]).values_list("answer_id",flat=True))
	if len(filtry)==2: id_filtered=(Result.objects.filter(parametres__Option_Code=filtry[0]).filter(parametres__Option_Code=filtry[1]).values_list("answer_id",flat=True))
	if len(filtry)==3: id_filtered=(Result.objects.filter(parametres__Option_Code=filtry[0]).filter(parametres__Option_Code=filtry[1]).filter(parametres__Option_Code=filtry[2]).values_list("answer_id",flat=True))		
	if len(filtry)==0: 
		filtry.append(0)
		filtry.append(0)
		filtry.append(0)		
	if len(filtry)==1: 
		filtry.append(0)
		filtry.append(0)
	if len(filtry)==2: 
		filtry.append(0)					
	data_filtered=(Result.objects.filter(answer_id__in=id_filtered))
	attribute_list=(data_filtered.values_list('parametres__Attribute__Attribute').distinct())	
	attributes_fin=(Attributes.objects.filter(id__in=attribute_list))	
	if request.GET.get("att")!=None: attribute_selected=int(request.GET.get("att"))
	if request.GET.get("att")==None: attribute_selected=1
	if attribute_selected!=999:
		option_list=sorted(list((data_filtered.filter(parametres__Attribute__Attribute=attribute_selected).values_list('parametres__Option_Code',flat=True).distinct())))
		options_fin=(Options.objects.filter(Option_Code__in=option_list))
		letter=0
		letters_fin=[]
		for i in options_fin:
			letter=letter+1
			letters_fin.append(colnum_string(letter))
		data=[]
		freq=[]
		freq_pct=[]
		count=[]
		column_num=0
		data.append((data_filtered.filter().values_list('result',flat=True)))	
		all_data=Result.objects.filter().values_list("result",flat=True)
		#if len(filtry)=1: data.append((data_filtered.objects.filter().values_list('result',flat=True)))			
		data_options=sorted(all_data.distinct())
		freq_total=Counter(data[0])
		freq_alldata=Counter(all_data)
		for i in option_list:
			data.append((data[0].filter(parametres__Option_Code=i).values_list('result',flat=True)))		
	if attribute_selected==999:
		if request.GET.get("time")!=None: timeframe_selected=int(request.GET.get("time"))		
		if request.GET.get("time")==None: timeframe_selected=1
		if timeframe_selected==2: option_list=data_filtered.dates('date_field', 'month')		
		if timeframe_selected==1: option_list=data_filtered.dates('date_field', 'month')		
		if timeframe_selected==3: option_list=data_filtered.dates('date_field', 'year')
		#data=Result.objects.filter(date_field__year='2016', date_field__month='6')
		options_fin=[]
		letter=0	
		if timeframe_selected==1 or timeframe_selected==3: 
			for month_year in option_list:
				if timeframe_selected==1: options_fin.append({'Option_Label':(str(month_year.month) + "-" + str(month_year.year)),'year':month_year.year,'month':month_year.month})
				if timeframe_selected==3: options_fin.append({'Option_Label':(str(month_year.year)),'year':month_year.year,'month':month_year.month})				
		if timeframe_selected==2:
			for month_year in option_list:
				if (month_year.month%3==1 and ({'Option_Label':(str((month_year.month+1)//3+1)  + "Q/" + str(month_year.year)),'year':month_year.year,'month':month_year.month+1}) not in options_fin): 
					options_fin.append({'Option_Label':(str((month_year.month+1)//3+1) + "Q/" + str(month_year.year)),'year':month_year.year,'month':month_year.month+1})
				if (month_year.month%3==2 and ({'Option_Label':(str((month_year.month)//3+1) + "Q/" + str(month_year.year)),'year':month_year.year,'month':month_year.month}) not in options_fin): 
					options_fin.append({'Option_Label':(str((month_year.month)//3+1) + "Q/" + str(month_year.year)),'year':month_year.year,'month':month_year.month})
				if (month_year.month%3==0 and ({'Option_Label':(str((month_year.month-1)//3+1) + "Q/" + str(month_year.year)),'year':month_year.year,'month':month_year.month-1}) not in options_fin): 
					options_fin.append({'Option_Label':(str((month_year.month-1)//3+1) + "Q/" + str(month_year.year)),'year':month_year.year,'month':month_year.month-1})
		data=[]
		freq=[]
		freq_pct=[]
		column_num=0	
		data.append((data_filtered.filter().values_list('result',flat=True)))	
		all_data=Result.objects.filter().values_list("result",flat=True)
		#if len(filtry)=1: data.append((data_filtered.objects.filter().values_list('result',flat=True)))			
		data_options=sorted(all_data.distinct())
		freq_total=Counter(data[0])
		freq_alldata=Counter(all_data)
		for month_year in options_fin:
			if timeframe_selected==1: data.append((data_filtered.filter(date_field__year=month_year['year'],date_field__month=month_year['month']).values_list('result',flat=True)))
			if timeframe_selected==2: data.append((data_filtered.filter(date_field__year=month_year['year'],date_field__month__in=quartal_months(month_year['month'])).values_list('result',flat=True)))			
			if timeframe_selected==3: data.append((data_filtered.filter(date_field__year=month_year['year']).values_list('result',flat=True)))						
		letters_fin=[]
		for i in options_fin:
			letter=letter+1
			letters_fin.append(colnum_string(letter))				
	for column in data:
		freq.append(Counter())
		freq[len(freq)-1].update(({x:0 for x in freq_alldata}))	
		freq[len(freq)-1].update(column)				
		freq_pct.append({})
		for freq_1 in freq[column_num]:
			if len(data[column_num])>0:	freq_pct[column_num][freq_1]=freq[column_num][freq_1]/len(data[column_num])
			if len(data[column_num])==0:	freq_pct[column_num][freq_1]=0
		freq_pct[column_num]['Total']=len(data[column_num])
		column_num=column_num+1
	results_fin=[]
	results_fin.append({'data':"/",'label':'Count','type':'freq'})		
	column_count=[]	
	chi_sig_9995=norm.ppf(0.9995)
	chi_sig_995=norm.ppf(0.995)
	chi_sig_975=norm.ppf(0.975)		
	for column in range(0, column_num):
		results_fin.append({'data':len(data[column]),'label':'Count','type':'index'})	
		column_count.append(len(data[column]))
	for data_one in data_options:
		results_fin.append({'data':"/",'label':Labels.objects.get(Attribute=question, Code=data_one)})
		for column in range(0, column_num):
			results_fin.append({'data':freq_pct[column][data_one]*100,'label':data_one,'type':'freq'})
			for column_sig in range(0, column_num):
					count_1=column_count[column]
					count_2=column_count[column_sig]
					abs_1=freq_pct[column][data_one]*count_1
					abs_2=freq_pct[column_sig][data_one]*count_2
					#print (((abs_2*count_1/count_2)*(1-abs_2/count_2)*(1-count_1/count_2)))			
					if count_2>0: square=((abs_2*count_1/count_2)*(1-abs_2/count_2)*(1-count_1/count_2))
					if count_2==0: square=0
					if square>=0: divider=sqrt(square)
					if square<0: divider=0
					if divider>0: chi_kvadrat=(abs_1-(abs_2*count_1/count_2))/divider
					if divider==0: chi_kvadrat=0			
					if chi_kvadrat<chi_sig_9995*-1 and column_sig==0: 
						results_fin[len(results_fin)-1]['sig_total_9995_minus']=1
					elif chi_kvadrat<chi_sig_995*-1 and column_sig==0: 
						results_fin[len(results_fin)-1]['sig_total_995_minus']=1
					elif chi_kvadrat<chi_sig_975*-1 and column_sig==0: 
						results_fin[len(results_fin)-1]['sig_total_975_minus']=1
					elif chi_kvadrat>chi_sig_9995 and column_sig==0: 
						results_fin[len(results_fin)-1]['sig_total_9995_plus']=1
					elif chi_kvadrat>chi_sig_995 and column_sig==0: 
						results_fin[len(results_fin)-1]['sig_total_995_plus']=1
					elif chi_kvadrat>chi_sig_975 and column_sig==0: 
						results_fin[len(results_fin)-1]['sig_total_975_plus']=1		
					if column-column_sig==1 and attribute_selected==999:									
						if chi_kvadrat>chi_sig_9995 and column_sig>0 and 'sig_9995_plus' not in (results_fin[len(results_fin)-1].keys()):  
							results_fin[len(results_fin)-1]['sig_9995_plus']="#8593"
						elif chi_kvadrat>chi_sig_995 and column_sig>0 and 'sig_995_plus' not in (results_fin[len(results_fin)-1].keys()):  
							results_fin[len(results_fin)-1]['sig_995_plus']="#8593"
						elif chi_kvadrat>chi_sig_975 and column_sig>0 and 'sig_975_plus' not in (results_fin[len(results_fin)-1].keys()):  
							results_fin[len(results_fin)-1]['sig_975_plus']="#8593"
						elif chi_kvadrat<chi_sig_9995*-1 and column_sig>0 and 'sig_9995_plus' not in (results_fin[len(results_fin)-1].keys()):  
							results_fin[len(results_fin)-1]['sig_9995_plus']="#8595"
						elif chi_kvadrat<chi_sig_995*-1 and column_sig>0 and 'sig_995_plus' not in (results_fin[len(results_fin)-1].keys()):  
							results_fin[len(results_fin)-1]['sig_995_plus']="#8595"
						elif chi_kvadrat<chi_sig_975*-1 and column_sig>0 and 'sig_975_plus' not in (results_fin[len(results_fin)-1].keys()):  
							results_fin[len(results_fin)-1]['sig_975_plus']="#8595"							
						elif chi_kvadrat>chi_sig_9995 and column_sig>0 and 'sig_9995_plus' in (results_fin[len(results_fin)-1].keys()):  
							results_fin[len(results_fin)-1]['sig_9995_plus']=results_fin[len(results_fin)-1]['sig_9995_plus']+colnum_string(column_sig)
						elif chi_kvadrat>chi_sig_995 and column_sig>0 and 'sig_995_plus' in (results_fin[len(results_fin)-1].keys()):  
							results_fin[len(results_fin)-1]['sig_995_plus']=results_fin[len(results_fin)-1]['sig_995_plus']+colnum_string(column_sig)
						elif chi_kvadrat>chi_sig_975 and column_sig>0 and 'sig_975_plus' in (results_fin[len(results_fin)-1].keys()):  
							results_fin[len(results_fin)-1]['sig_975_plus']=results_fin[len(results_fin)-1]['sig_975_plus']+colnum_string(column_sig)			
					if attribute_selected!=999:
						if chi_kvadrat>chi_sig_9995 and column_sig>0 and 'sig_9995_plus' not in (results_fin[len(results_fin)-1].keys()):  
							results_fin[len(results_fin)-1]['sig_9995_plus']=colnum_string(column_sig)
						elif chi_kvadrat>chi_sig_995 and column_sig>0 and 'sig_995_plus' not in (results_fin[len(results_fin)-1].keys()):  
							results_fin[len(results_fin)-1]['sig_995_plus']=colnum_string(column_sig)
						elif chi_kvadrat>chi_sig_975 and column_sig>0 and 'sig_975_plus' not in (results_fin[len(results_fin)-1].keys()):  
							results_fin[len(results_fin)-1]['sig_975_plus']=colnum_string(column_sig)			
						elif chi_kvadrat>chi_sig_9995 and column_sig>0 and 'sig_9995_plus' in (results_fin[len(results_fin)-1].keys()):  
							results_fin[len(results_fin)-1]['sig_9995_plus']=results_fin[len(results_fin)-1]['sig_9995_plus']+colnum_string(column_sig)
						elif chi_kvadrat>chi_sig_995 and column_sig>0 and 'sig_995_plus' in (results_fin[len(results_fin)-1].keys()):  
							results_fin[len(results_fin)-1]['sig_995_plus']=results_fin[len(results_fin)-1]['sig_995_plus']+colnum_string(column_sig)
						elif chi_kvadrat>chi_sig_975 and column_sig>0 and 'sig_975_plus' in (results_fin[len(results_fin)-1].keys()):  
							results_fin[len(results_fin)-1]['sig_975_plus']=results_fin[len(results_fin)-1]['sig_975_plus']+colnum_string(column_sig)		
	prom_nps=[]
	detr_nps=[]
	pass_nps=[]
	nps_fin=[]
	column_num=0	
	for column in freq_pct:
		prom_nps.append({})
		detr_nps.append({})		
		pass_nps.append({})				
		nps_fin.append({})
		prom_nps[column_num]['Promoters']=boxes(freq_pct[column_num],[10,11])
		pass_nps[column_num]['Passives']=boxes(freq_pct[column_num],[8,9])			
		detr_nps[column_num]['Detractors']=boxes(freq_pct[column_num],[1,2,3,4,5,6,7])					
		nps_fin[column_num]['NPS']=prom_nps[column_num]['Promoters']-detr_nps[column_num]['Detractors']
		column_num=column_num+1	
	results_fin.append({'data':"/",'label':'Promoters','type':'freq'})
	for column in range(0, column_num):
		results_fin.append({'data':prom_nps[column]['Promoters']*100,'label':'Promoters','type':'freq'})				
		for column_sig in range(0, column_num):
			sign (column, column_sig, prom_nps[column]['Promoters'],prom_nps[column_sig]['Promoters'])	
	results_fin.append({'data':"/",'label':'Passives','type':'freq'})
	for column in range(0, column_num):
		results_fin.append({'data':pass_nps[column]['Passives']*100,'label':'Passives','type':'freq'})	
		for column_sig in range(0, column_num):
			sign (column, column_sig, pass_nps[column]['Passives'],pass_nps[column_sig]['Passives'])			
	results_fin.append({'data':"/",'label':'Detractors','type':'freq'})
	for column in range(0, column_num):
		results_fin.append({'data':detr_nps[column]['Detractors']*100,'label':'Detractors','type':'freq'})	
		for column_sig in range(0, column_num):
			sign (column, column_sig, detr_nps[column]['Detractors'],detr_nps[column_sig]['Detractors'])		
	results_fin.append({'data':"/",'label':'NPS','type':'index'})			
	for column in range(0, column_num):
		results_fin.append({'data':nps_fin[column]['NPS']*100,'label':'NPS','type':'index'})	
		for column_sig in range(0, column_num):
			sign (column, column_sig,(nps_fin[column]['NPS']+1)/2,(nps_fin[column_sig]['NPS']+1)/2)													
	results_fin.append({'data':"/",'label':'Mean','type':'mean'})						
	for column in range(0, column_num):
		if len(data[column])>0: results_fin.append({'data':mean(data[column]),'label':'Mean','type':'mean'})		
		if len(data[column])<1: results_fin.append({'data':"N/A",'label':'Mean','type':'mean'})				
	results_fin.append({'data':"/",'label':'Std. Dev.','type':'stdev'})						
	for column in range(0, column_num):
		if len(data[column])>1: results_fin.append({'data':stdev(data[column]),'label':'Std. Dev.','type':'stdev'})		
		if len(data[column])<=1: results_fin.append({'data':"N/A",'label':'Std. Dev.','type':'stdev'})								
	print("--- %s seconds ---" % (time.time() - start_time))
	if attribute_selected!=999:	
		return render(request, "test_all_rows.html", {"filters_selected1":int(filtry[0]),"filters_selected2":int(filtry[1]),"filters_selected3":int(filtry[2]),"filters":all_options_fin,"attributes": attributes_fin, "attribute_selected":attribute_selected,"options":options_fin,"nps":results_fin,"letters":letters_fin,"sig_total":sig_total,"sig_paired":sig_paired})
	if attribute_selected==999:
		return render(request, "test_all_rows.html", {"filters_selected1":int(filtry[0]),"filters_selected2":int(filtry[1]),"filters_selected3":int(filtry[2]),"filters":all_options_fin,"attributes": attributes_fin, "attribute_selected":attribute_selected,"options":options_fin,"nps":results_fin,"timeframe_selected":timeframe_selected,"letters":letters_fin,"sig_total":sig_total,"sig_paired":sig_paired})