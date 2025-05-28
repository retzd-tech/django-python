from django.shortcuts import render, redirect
from .models import CrawlResult
from .crawler import fetch_and_parse

def crawl(request):
    if request.method == "POST":
        url = request.POST["url"]
        result = fetch_and_parse(url)
        CrawlResult.objects.create(**result)
        return redirect('crawl')  # redirect back to the same form page
    
    return render(request, "crawl_form.html", {
        "results": CrawlResult.objects.order_by("-fetched_at")[:10]
    })