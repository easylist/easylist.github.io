Who does anti-Adblock actually affect?
######################################

:date: 2010-12-21 07:47
:tags: Adblock Plus, known issues
:category: Articles
:slug: 2010/12/21/who-does-anti-adblock-actually-affect
:authors: Michael

Anti-Adblock scripts, which attempt to identify users of advert-blocking software and limit or, more commonly, disable access to content, appear to have become increasingly prevalent recently. Yet the techniques used to detect unwanted software are by no means infallible, and I have seen, on several occasions, that while they are certainly targeting particular groups of people, this has tended to include many innocent bystanders. I have therefore decided to outline the visitors who I believe are usually affected by such additional website "functionality".

**People with scripting disabled**
  It is not uncommon for JavaScript to be disabled for reasons of security, with one of the most used Firefox add-ons, `NoScript`_, being available specifically for this purpose. As anti-Adblock nearly always requires client scripting in order to detect advert filtration, it can just as easily cause problems for any security-conscious members of the online community [*]_.

**People with special software requirements**
  Not everyone accesses the internet in exactly the same manner; some out of choice, some out of necessity. People in the latter group usually have a disability that prevents them from being able to interpret web pages as provided in standard browsers, and therefore may use alternatives to cater for their needs. However, as anti-Adblock techniques usually assume that there is only one possible display of a page, something that is simply inaccurate given that HTML, by definition, only marks pages rather than precisely defines them, people with customised web browsers may also be prevented from viewing page content. One of the most ludicrous examples that I have encountered is a site aimed at blind people that pointlessly mandates that all images are loaded in order to permit the textual content to be displayed.

**People with poor connections to the website**
  Anti-Adblock techniques usually revolve around loading an item with a name that would usually be blocked by filter subscriptions and subsequently detecting whether or not it is present; however, this relies on the object being immediately available to be scrutinised. There are two reasons why this may not occur: the first is that the client could be using a dial-up internet connection and the second is a reliance on a particular server being constantly available for communicating data, a problem only exacerbated when the item is hosted on a third-party domain. Relying on these two suppositions is extremely risky, as no hosting or internet service provider can guarantee 100% up time or that every connection will be successful.

**Search engine spiders**
  Search engine spiders usually only record the text of a page, with Google noting that "`fancy features such as JavaScript [mean that] search engine spiders may have trouble crawling your site`_" ; however, requiring every item to be loaded on a domain, something that a bot may not do, means that all that the search engine will record is that advert blocking programs must not be used. This damages any search result rankings applied to the content because there is no relevant text to analyse and could consequently worsen the position of the domain when a particular term is requested.

As the above list demonstrates, there are many innocent people who are affected by attempts to implement anti-Adblock on a domain. The irony is that visitors with sufficiently advanced advert-blocking software are usually unaffected by such measures because of the presence of whitelists that protect necessary items and automatically updating subscriptions that distribute alterations negating detection.

So when you next consider adding anti-Adblock to a website, please first consider you you are actually going to cause problems for: visitors blocking adverts, people with slow internet connections or disabilities, or your own search engine reputation.

.. _`Noscript`: https://addons.mozilla.org/en-US/firefox/addon/722/
.. [*] Incidentally, some people remove adverts to decrease the number of attack vectors available when visiting a website, and therefore can also fall into the category of "security-conscious" visitors.
.. _`fancy features such as JavaScript [mean that] search engine spiders may have trouble crawling your site`: http://www.google.com/support/webmasters/bin/answer.py?answer=35769
