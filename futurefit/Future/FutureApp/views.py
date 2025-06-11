# Create your views here.
from django.shortcuts import render
from .models import NewsUpdate,NewsletterSubscription,ContactUs, Store, StudyAbroadFormSubmission, GetInTouchFormSubmission, ProgramApplication
from .forms import ContactUsForm,NewsletterSubscriptionForm, StudyAbroadForm, GetInTouchForm, ProgramApplicationForm
from django.http import JsonResponse
from django.contrib import messages
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
def home_view(request):
    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for subscribing!")
            form = NewsletterSubscriptionForm()  # reset form
        else:
            messages.error(request, "Please enter a valid email.")
    else:
        form = NewsletterSubscriptionForm()
    
    return render(request, 'FutureApp/home.html', {'form': form})

def about_us_view(request):
    return render(request, 'FutureApp/about_us.html')

def our_service_view(request):
    return render(request, 'FutureApp/our_service.html')

def programs_view(request):
    return render(request, 'FutureApp/programs.html')

def study_abroad_view(request):
    if request.method == 'POST':
        form = StudyAbroadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your application has been submitted successfully!")
            form = StudyAbroadForm()  # Reset form
        else:
            messages.error(request, "Please correct the errors in the form.")
    else:
        form = StudyAbroadForm()
    
    return render(request, 'FutureApp/study_abroad.html', {'form': form})
    

   
def energy_solution_view(request):
    if request.method == 'POST':
        try:
            GetInTouchFormSubmission.objects.create(
                first_name=request.POST.get('first_name'),
                last_name=request.POST.get('last_name'),
                email=request.POST.get('email'),
                phone_number=request.POST.get('phone_number'),
                purpose=request.POST.get('purpose'),
                message=request.POST.get('message'),
            )
            messages.success(request, 'Thank you! Your message has been sent successfully.')
            return redirect('energy_solution_view')  # Clears the form
        except Exception as e:
            messages.error(request, f'An error occurred: {e}')
    
    return render(request, 'FutureApp/energy_solution_view.html')




def store_view(request):
    return render(request, 'FutureApp/store.html')


def news_update_view(request):
    posts = NewsUpdate.objects.order_by('-date_published')
    return render(request, 'FutureApp/news_update.html', {'posts': posts})


def news_detail_view(request, slug):
    post = get_object_or_404(NewsUpdate, slug=slug)
    return render(request, 'FutureApp/news_detail.html', {'post': post})

    
def ai_page(request):
    return render(request, 'FutureApp/ai.html')


def emb(request):
    return render(request, 'FutureApp/emb.html')

def three_d(request):
    return render(request, 'FutureApp/three_d.html')

def python_page(request):
    return render(request, 'FutureApp/python.html')




class contact_view(FormView):
    template_name = 'FutureApp/ContactUs.html'    
    form_class = ContactUsForm
    success_url = reverse_lazy('contact')  # Redirect after successful form submission

    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, "Your message has been sent successfully!") 
        return super().form_valid(form)

def newsletter_subscribe_view(request):
    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you for subscribing!")
            form = NewsletterSubscriptionForm()  # reset form
        else:
            messages.error(request, "Please enter a valid email.")
    else:
        form = NewsletterSubscriptionForm()

    return render(request, 'FutureApp/home.html', {'form': form})


def store_view(request):
    items = Store.objects.all()
    return render(request, 'FutureApp/store.html', {'items': items})

def store_detail(request, slug=None, pk=None):
    if slug:
        item = get_object_or_404(Store, slug=slug)
    elif pk:
        item = get_object_or_404(Store, pk=pk)
    else:
        return render(request, '404.html', status=404)

    return render(request, 'FutureApp/store_detail.html', {'item': item})



def add_to_cart(request, item_id):
    if request.method == 'POST':
        item = get_object_or_404(Store, id=item_id)
        quantity = int(request.POST.get('quantity', 1))
        cart = request.session.get('cart', {})
        item_key = str(item_id)

        if item_key in cart:
            cart[item_key]['quantity'] += quantity
        else:
            cart[item_key] = {
                'name': item.name,
                'price': float(item.price),
                'quantity': quantity,
            }

        request.session['cart'] = cart

        return JsonResponse({
            'name': item.name,
            'price': float(item.price),
            'quantity': cart[item_key]['quantity'],
        })



def get_in_touch_view(request):
    if request.method == 'POST':
        form = GetInTouchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_in_touch_success')  # Define this URL
    else:
        form = GetInTouchForm()
    return render(request, 'FutureApp/get_in_touch.html', {'form': form})

def apply_program(request):
    form = ProgramApplicationForm()
    success = False
    show_modal = False

    if request.method == 'POST':
        form = ProgramApplicationForm(request.POST, request.FILES)
        show_modal = True  # Always show modal on POST
        if form.is_valid():
            form.save()
            success = True
            form = ProgramApplicationForm()  # Reset the form
            # Do not show modal after success; or keep it open if you prefer
            show_modal = True

    return render(request, 'FutureApp/program_application.html', {
        'form': form,
        'success': success,
        'show_modal': show_modal
    })