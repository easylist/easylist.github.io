EasyList Statistics: August 2011
################################

:date: 2011-09-01 12:00
:tags: EasyList, EasyPrivacy, EasyList Germany
:category: Articles
:slug: 2011/09/01/easylist-statistics:-august-2011
:authors: Michael

Looking back, it has been `a long time since`_ anyone has evaluated or released the statistics for the EasyList subscriptions, so I thought that, as August has just eneded, it might be time to estimate exactly how many users there are of the filter lists.

Even though I am aware that most people are interested simply in the user estimates, I should start by explaining how the statistics are gathered for the users of EasyPrivacy and any other privacy conscious individuals. When a browser connects to a web server, it automatically sends information to request a copy of, in this instance, a text file. This request includes the user agent, which for Firefox states the name of the operating system (although this information is not present in my statistics) and the version of the browser. The Adblock Plus website, like so many others, logs these requests with the time and date the request was made. These logs are then analysed by `AWStats`_. No active tracking scripts have been installed.

Although there is a lot of information, calculating the number of users of the EasyList subscriptions cannot provide a complete picture for a variety of reasons. Adblock Plus updates subscriptions between four and six days after they were last updated. However, if a user does not use a browser for a day, then an update will be delayed for a day, up to ten days after a subscription was last updated. This being August, many people are likely to be on holiday, which means that the subscription updates are likely to be less frequent than my assumed value of five days. It is also possible, but extremely unlikely, that results may be overestimated as a result of many people forcing a download from the Adblock Plus preferences window.

Viewing the statistics at the time this algorithm was implemented, `Wladimir hoped that the changes would prevent a “Monday peak”`_ from overloading the server, the result of office workers all updating on Monday morning if the five day interval passed over the weekend. However, it is clear that there are a number of users of the subscriptions who do not have a recent version of Adblock Plus installed. Using the four full weeks of August 2011 as an example, Mondays show on average 12% more downloads than would be expected (week total / 7), ranging from 110.8% to 118.5% of the expected traffic. In contrast, downloads tended to tail off as the week progressed, the most marked drop being on Saturdays and Sundays, with an average of 92% of the expected traffic each day. This ranged from a low of 91.6% on Saturday 13 August to a weekend high of 95.8% on Sunday 28 August.

In spite of the variation based on week day the total number of downloads per week was fairly stable: in order, each week achieved 98.1%, 99.0%, 100.7% and 102.2% of expected traffic, the initial low results likely the results of holidays without computers and therefore without updates to EasyList.

Now, however, it is time to answer the big question: how many people actually use the subscriptions? These values were calculated by taking the total number of downloads in a month, dividing the resulting total by thirty one to find the average number per day and then multiplying by five, as this would be, if everyone used their browser daily (which they don't), the average update period.

Going through the subscriptions, it is no surprise that `EasyList`_ has the largest user base. Taking into account all combined subscriptions, versions and variations, such as the one with element hiding rules, the one without rules for adult websites and relevant tracking protection lists, we find that there were seventy three million downloads of the file in August, suggesting that there are **twelve million users**, of whom 99% use Adblock Plus filter format. `EasyList Germany`_ has also been popular, with two and a half million users (99.9% Adblock Plus format), as has `EasyPrivacy`_, despite the comparatively paltry total of "just" half a million users. However, unlike EasyList and EasyList Germany, which have seen little usage as Tracking Protection Lists, just over half of the users of EasyPrivacy use `EasyPrivacy TPL`_, its popularity likely due to `Microsoft's promotion of the list`_, which we are very grateful for.

Next, it is possible to put these values in perspective: how dominant is EasyList as an Adblock Plus subscription? Looking at `the public statistics page for the add-on`_ and ignoring the recent erroneous readings, we find that there are twelve and a half million users of Adblock Plus. Taking into account the usage of AdBlock for Chrome and Adblock Plus for Chrome, which according to user agents accounts for, at most, 15% of installations, we find that 80% of people using Adblock Plus use EasyList as a primary subscription. This is despite the random selection of EasyList or Fanboy's List for a new English language user. I would attribute this popularity to historical reasons (people installed Adblock Plus when EasyList was the only recommended subscription for English language users); the large number of recommended supplementary subscriptions, including `EasyList Germany`_, `RU AdList`_, `Liste FR`_ and `ChinaList`_ [*]_, to name but a few, which are selected automatically when the subscription and browser languages match; and its position as a fallback subscription: if the browser language does not match any recommended subscription, EasyList is automatically installed.

Of course, the minor subscriptions also deserve a mention. `EasyList without element hiding`_ has accumulated around seven thousand users, `EasyList without rules for adult sites`_ has over two thousand users and EasyPrivacy without international filters has just over one thousand users. Finally, `EasyTest`_, an EasyList supplement used for examining filters known to cause problems on websites, has accumulated just 33 users.

While there is great variation in the usage of the EasyList subscriptions, the statistics emphasise the great responsibility that we authors have - a minor mistake can quickly affect thousands of people. I would therefore appeal to anyone who has made it to the final paragraph to consider getting involved with the project to assist the very few authors we have - even suggesting rules for problematic sites helps us to reduce the time it takes to commit a fix. Regardless of this challenge, I am optimistic:  provided the requisite bandwidth is made available (4.2 TB was required this month for the Adblock Plus version of EasyList alone), I see no reason why the project should not continue to be successful.

.. [*] I am not going to discuss the usage of the affiliated subscriptions as I do not have the statistics for the files hosted third-party, but the subscription authors are welcome to write their own analysis with the assistance of statistics for the EasyList mirrors - you should know how to access the logs, if not, please private message me.

.. _`a long time since`: https://forums.lanik.us/viewtopic.php?t=679
.. _`AWStats`: http://awstats.sourceforge.net/
.. _`Wladimir hoped that the changes would prevent a “Monday peak”`: https://adblockplus.org/blog/downloading-a-file-regularly-how-hard-can-it-be
.. _`EasyList`: https://easylist.adblockplus.org/#easylist
.. _`EasyList Germany`: https://easylist.adblockplus.org/#easylistgermany
.. _`EasyPrivacy`: https://easylist.adblockplus.org/#easyprivacy
.. _`EasyPrivacy TPL`: https://easylist.adblockplus.org/blog/2011/02/10/easyprivacy-tracking-protection-list
.. _`Microsoft's promotion of the list`: https://ie.microsoft.com/testdrive/Browser/TrackingProtectionLists/
.. _`RU AdList`: https://code.google.com/p/ruadlist/
.. _`Liste FR`: http://adblock-listefr.com/
.. _`ChinaList`: https://code.google.com/p/adblock-chinalist/
.. _`the public statistics page for the add-on`: https://addons.mozilla.org/statistics/addon/1865
.. _`EasyList without element hiding`: https://easylist.adblockplus.org/#easylistnoelemhide
.. _`EasyList without rules for adult sites`: https://easylist.adblockplus.org/blog/2011/05/30/announcing-easyadult
.. _`EasyTest`: https://forums.lanik.us/viewtopic.php?t=8505
