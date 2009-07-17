from page.models import PageDisplay
from score.models import Score, ScoreType
from django.shortcuts import render_to_response
from django.template import RequestContext
from company.models import Company
from campaign.models import Campaign

# For handling content to file type conversion
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage as s3_storage
from django.core.cache import cache

# For converting relative to absolute URLs
import lxml.html

# For generating random filenames
import hashlib
import random

# For doing screen shot script through CLI
import os


def new(request, template_name="new.html"):
    """
    Handles new requests
    """
    #if request.method == 'POST':
    
    url = request.REQUEST["url"]
    
    #import pdb; pdb.set_trace();

    try:
        affiliate_id = request.REQUEST["affiliate_id"]
    except:
        affiliate_id = 1

    affiliate = Company.objects.get(id=affiliate_id)
    
    try:
        campaign_id = request.REQUEST["campaign_id"]
    except:
        campaign_id = 1
    
    campaign = Campaign.objects.get(id=campaign_id)

    try:
        platform = request.REQUEST["platform"]
    except:
        platform = ''
        
    try:
        user_agent = request.REQUEST["userAgent"]
    except:
        user_agent = ''
        
    try:
        app_version = request.REQUEST["appVersion"]
    except:
        app_version = ''
        
    try:
        app_name = request.REQUEST["appName"]
    except:
        app_name = ''
    
    try:
        app_code_name = request.REQUEST["appCodeName"]
    except:
        app_code_name = ''
        
    try:
        html_str = request.REQUEST["html"]
    except:
        html_str = ''
 
    html_str = lxml.html.fromstring(html_str)
    html_str.make_links_absolute(url)
    content = lxml.html.tostring(html_str)
    
    filename = hashlib.sha1(str(random.random())).hexdigest()
    
    filename_html = 'tester/' + filename + '.html'

    filename_png = "file:///users/adam/Documents/workspace/performline-albatross/src/pinax/falcon/" + filename + "-full.png"

    page = PageDisplay(affiliate=affiliate,campaign=campaign,url=url,
                       content_local=content,image_url=filename_png,
                       platform=platform,user_agent=user_agent,
                       app_version=app_version,app_name=app_name,
                       app_code_name=app_code_name,score=50)
    
    page.content.save(filename_html, ContentFile(content))
    
    # Todo: total hack - we need something that works on Mac/Linux (or at least Linux) and a library rather than CLI
    cli = "/Users/adam/webkit2png.py --delay=2 --fullsize --filename=" + filename + " https://renderadamperformlinecomroot.s3.amazonaws.com:443/performline_page_source/" + filename + ".html"
    os.system(cli)


    test_requester = 'tester'
    return render_to_response(template_name, {
        "request": test_requester
    }, context_instance=RequestContext(request))
