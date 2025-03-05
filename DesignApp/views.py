from django.shortcuts import render, redirect
from AdminApp.models import DesignCategoryDb, DesignsDb, DailyProgressDb
from DesignApp.models import ConsultDb
from WebApp.models import UserRegistrationDb
from django.contrib import messages


# for pdf generation
# from django.template.loader import render_to_string
from django.http import HttpResponse
from xhtml2pdf import pisa


# Create your views here.
def category_page(request):
    data = DesignCategoryDb.objects.all()
    return render(request, "category.html", {'data': data})


def filter_design(request, ct_name):
    data = DesignsDb.objects.filter(Category=ct_name)
    name = ct_name
    return render(request, "design_page.html", {'data': data, 'name': name})


def design_single(request, d_id):
    item = DesignsDb.objects.get(id=d_id)

    # Update browsing history in session
    if 'browsing_history' not in request.session:
        request.session['browsing_history'] = []
    if d_id not in request.session['browsing_history']:
        request.session['browsing_history'].append(d_id)
        request.session.modified = True  # Ensure the session is saved

    # Limit the browsing history to the most recent 5 items
    if len(request.session['browsing_history']) > 5:
        request.session['browsing_history'] = request.session['browsing_history'][-5:]

    recommendations = get_recommendations(request)

    return render(request, "design_single.html", {'item': item, 'recommendations': recommendations})


def get_recommendations(request):
    browsing_history = request.session.get('browsing_history', [])
    if browsing_history:
        # Get recommended items (e.g., similar categories or designs)
        # Fetch recommendations excluding the most recent item and reverse the order
        recommendations = DesignsDb.objects.filter(id__in=browsing_history[:-1]).order_by('-id')

    else:
        recommendations = DesignsDb.objects.all()[:4]  # Default recommendation

    print(list(i.id for i in recommendations))
    return recommendations


def consultation_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        location = request.POST.get('location')
        design_category = request.POST.get('design_category')
        design_name = request.POST.get('design_name')
        design_id = request.POST.get('design_id')
        design_estimate = request.POST.get('design_estimate')
        design_dimension = request.POST.get('design_dimension')
        un = request.session['username']
        # user = UserRegistrationDb.objects.get(username=un)

        # Save data to ConsultDb
        consult_entry = ConsultDb(name=name, email=email, mobile=mobile, location=location, design_id=design_id,
                                  design_category=design_category, design_name=design_name,
                                  design_estimate=design_estimate, design_dimension=design_dimension, username=un)
        consult_entry.save()
        messages.success(request, "Booked your Consultation. We will reach you soon")

        return redirect(category_page)


def download_design_pdf(request, d_id):
    # Fetch the design object from the database
    design = DesignsDb.objects.get(id=d_id)

    # Render the HTML content
    html_content = render(request, 'download_design_pdf.html', {'design': design})

    # Create a response to send the PDF as a downloadable file
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="design_{design.id}.pdf"'

    # Convert HTML to PDF using xhtml2pdf
    pisa_status = pisa.CreatePDF(html_content.content.decode('utf-8'), dest=response)

    if pisa_status.err:
        return HttpResponse('Error generating PDF', status=500)

    return response


# interior design booked section
def booked_design_page(request):
    un = request.session['username']
    data = ConsultDb.objects.filter(username=un)
    return render(request, "my_design_bookings.html", {'data': data})


def daily_progress(request, c_id):
    consult = ConsultDb.objects.get(id=c_id)
    # design = DailyProgressDb.objects.filter(consult=consult)
    design = DailyProgressDb.objects.filter(consult=consult).order_by('-TimeStamp')
    return render(request, "design_daily_progress.html", {'design': design, 'consult': consult})

# Estimate Calculate section


def estimate_page(request):
    return render(request, "estimate_calculate_page.html")


def calculate_estimate(request):
    if request.method == "POST":
        kit = request.POST.get('kitchen')
        bed = request.POST.get('bedroom')
        bath = request.POST.get('bathroom')
        liv = request.POST.get('living')
        wardrobe = request.POST.get('wardrobe')
        tv = request.POST.get('tv')

        essential = float(int(kit) * .45 + int(bed) * .35 + int(bath) * .25 + int(liv) * .25 + int(wardrobe) * .1 + int(tv) * .1)
        premium = float(int(kit) * .65 + int(bed) * .45 + int(bath) * .35 + int(liv) * .35 + int(wardrobe) * .15 + int(tv) * .15)
        luxury = float(int(kit) * .95 + int(bed) * .75 + int(bath) * .6 + int(liv) * .55 + int(wardrobe) * .35 + int(tv) * .3)

        essential = round(essential, 4)
        premium = round(premium, 4)
        luxury = round(luxury, 4)

        return render(request, "estimate_display.html", {'essential': essential, 'premium': premium, 'Luxury': luxury})


