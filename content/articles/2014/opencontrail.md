Title: OpenContrail developper of the month
Date: 2014-05-01 20:32
Author: Sebastien Badia
About_author: Cloud engineer @eNovance, Puppet addict and Net Neutrality defender.
Category: Seb
Tags: OpenContrail, Debian
Slug: opencontrail-juniper

## Outline

Une petit interview en anglais à propos du packaging d'OpenContrail. Publiée sur le [blog d'OpenContrail](http://opencontrail.org/developer-spotlight/developer_spotlight_may_2014/) et sur le [blog de CloudWatt](http://blog.cloudwatt.com/fr/opencontrail/2014/05/12/sebastien-Badia-opencontrail-developer-of-the-month.html).

# Developer Spotlight May 2014 – Sébastien Badia

## About Sébastien Badia

Sébastien (Seb) Badia is a Software / Systems Engineer at eNovance, Paris France based. Sébastien Badia provider of open cloud computing software. Seb concentrates on projects including packaging, system administration (automation, configuration management, ci) and OpenStack in general. Seb is a co-founder of the non-profit organization LDN, Lorraine Data Network, which is a neutral and open Internet access provider. In addition, he is actively involved in the Federation FDN, a federation of 25 non-profit Internet access providers around France, and also makes contributions to Gitoyen (an alternative network operator) and Debian (open operating system initiative).

## About eNovance

eNovance deploys its services around two lines of business, the first one is around the development, integration, operation and support of cloud computing infrastructure for Private Cloud uses or for Public Cloud Services Providers. The second line of business is on distributing and managing critical web applications on the world’s largest Public Clouds such as AWS, Google Compute Engine, RackSpace, Cloudwatt and more. In less than 3 years, eNovance has become the 7th largest global contributor to the OpenStack initiative and the only Europe based company to serve on the board of directors of OpenStack.

## Interview

### How did you first hear about OpenContrail and what was your initial reaction?

In the scope of eNovance service for CloudWatt, I attended a CloudWatt session on SDN and networks overview (MPLS/BGP) where the speaker also spoke about OpenContrail and gave us the pointer on the OpenContrail [ebook](http://opencontrail.org/ebook/) gave me real clear and concise view of the OpenContrail project and its capabilities. It was very interesting, and I wanted to know more about it.

### What made you decide to download the OpenContrail code and play around with it? Any particular driver or work initiative?

CloudWatt had studied the corporate version of OpenContrail, but the real trigger was the opening of the code with Apache2 license. OpenContrail was open, very easy to download and deploy, so, we decided to contribute to the packaging effort launched by Pedro Marques. Together with Romain V. from CloudWatt and Sylvain B., we also created a continuous integration system to builder packages, which was installed on a pool of nodes to verify the installation. This capability allowed us to quickly converge on the remaining software development and testing efforts.

### What work have you done with the OpenContrail code?  Tell us about it and what value it might have to others?

I worked with Pedro M. and Ted G. on the [packaging](https://github.com/Juniper/contrail-packages/) of the community version of OpenContrail. We have made a lot of enhancements together and we will soon release 1.06 version which will be the first community version of OpenContrail.  PPA (Personal Package Archives) has been created (ppa:contrail/ppa) to enable installation of OpenContrail with just an « apt-get » command without the need to compile all the code. Using the capabilities of a simple configuration management tool, we will be enabling very easy installation of OpenContrail by handling the packaging and management of all dependencies including those even in upstream distributions. Debian and Ubuntu will receive these packaging enhancements soon based on the normal cycle releases.

### What has been your experience in working with the OpenContrail team?

OpenContrail team was very productive and dynamic, either on the mailing list or IRC, with relevant and interesting information exchanges! Regular [weekly meetings on IRC](http://opencontrail.org/opencontrail-weekly-meeting) has been extremely useful. I mostly worked with Pedro, and it was very interesting, we extensively used the reviews system to take advantage of the different time zones, and of course to validate each other.

### What would you like to see improved with the OpenContrail code or overall community?

Maybe a continuous Integration system like the one OpenStack has, that has reviewing capabilities providing a clear view of patch set, well integrated with bug tracker, and of course pre-merge validation functionality. But I was also informed that this capability will be coming soon. A unique place for documentation would also be a good improvement similar to what [OpenStack’s](http://docs.openstack.org), as currently some of the documentation is inside a github wiki, and some other parts are on [OpenContrail](http://www.opencontrail.org) website.

### What do you think the real value of SDN or NFV will be for you or your industry?

[Cloudwatt](http://cloudwatt.com) is a cloud provider based in France and they use SDN as the backbone of their cloud solution. SDN basically allows Cloudwatt to provide virtual private networks inside the datacenter and cross-datacenters. NFV is the next step, we will soon work on service VM insertion using routing policies. In short SDN makes network easy to provision, easy to upscale.

### What is your overall perception of the importance of open source in SDN/networking/technology/innovation?

There would be no Internet as we know it today without free software, both are inseparable (RFC based, open standard), Free and open software is a great vector for sustainability and development, I am very pleased that Juniper goes in this direction because it will facilitate interoperability between existing open source network solutions with high performance Juniper hardware.
