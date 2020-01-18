%global namedreltag .Final
%global namedversion %{version}%{namedreltag}
%global prodname resteasy

Name:           resteasy-base
Version:        3.0.6
Release:        4%{?dist}
Summary:        Framework for RESTful Web services and Java applications
License:        ASL 2.0 and CDDL
URL:            http://www.jboss.org/resteasy

# git clone git://github.com/resteasy/Resteasy.git
# cd Resteasy
# git archive --prefix=resteasy-3.0.6.Final/ --output=resteasy-3.0.6.Final.tar.gz 3.0.6.Final
Source0:        %{prodname}-%{namedversion}.tar.gz
Patch0:         0001-Mime4j-0.7.2-support.patch
Patch1:         0002-bcmail-api-change.patch
Patch2:		%{prodname}-%{namedversion}-resteasy-1073.patch
Patch3:         %{prodname}-%{namedversion}-resteasy-1280539.patch
Patch4:         %{prodname}-%{namedversion}-resteasy-1357624.patch
Patch5:         %{prodname}-%{namedversion}-resteasy-1378619.patch

BuildArch: noarch

BuildRequires:  maven-local
BuildRequires:  mvn(com.sun.xml.bind:jaxb-impl)
BuildRequires:  mvn(commons-httpclient:commons-httpclient)
BuildRequires:  mvn(javax.servlet:servlet-api)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(log4j:log4j)
BuildRequires:  mvn(org.apache.httpcomponents:httpclient)
BuildRequires:  mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-deploy-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-install-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-javadoc-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.codehaus.jackson:jackson-core-asl)
BuildRequires:  mvn(org.codehaus.jackson:jackson-jaxrs)
BuildRequires:  mvn(org.codehaus.jackson:jackson-mapper-asl)
BuildRequires:  mvn(org.codehaus.jackson:jackson-xc)
BuildRequires:  mvn(org.codehaus.jettison:jettison)
BuildRequires:  mvn(org.jboss.spec.javax.annotation:jboss-annotations-api_1.1_spec)
BuildRequires:  mvn(org.jboss.spec.javax.servlet:jboss-servlet-api_2.5_spec)
BuildRequires:  mvn(org.scannotation:scannotation)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.jboss:jandex)

Requires:       resteasy-base-jaxrs-api         = %{version}-%{release}
Requires:       resteasy-base-providers-pom     = %{version}-%{release}
Requires:       resteasy-base-atom-provider     = %{version}-%{release}
Requires:       resteasy-base-jackson-provider  = %{version}-%{release}
Requires:       resteasy-base-jaxb-provider     = %{version}-%{release}
Requires:       resteasy-base-jaxrs             = %{version}-%{release}
Requires:       resteasy-base-jaxrs-all         = %{version}-%{release}
Requires:       resteasy-base-jettison-provider = %{version}-%{release}
Requires:       resteasy-base-tjws              = %{version}-%{release}
Requires:	resteasy-base-client		= %{version}-%{release}
Requires:	resteasy-base-resteasy-pom	= %{version}-%{release}


%description
%global desc \
RESTEasy contains a JBoss project that provides frameworks to help\
build RESTful Web Services and RESTful Java applications. It is a fully\
certified and portable implementation of the JAX-RS specification.
%{desc}
%global extdesc %{desc}\
\
This package contains

%package        javadoc
Summary:        Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%package        jaxrs-api
Summary:        Module jaxrs-api for %{name}

%description    jaxrs-api
%{extdesc} %{summary}.

%package        providers-pom
Summary:        Module providers-pom for %{name}

%description    providers-pom
%{extdesc} %{summary}.

%package        atom-provider
Summary:        Module atom-provider for %{name}

%description    atom-provider
%{extdesc} %{summary}.

%package        jackson-provider
Summary:        Module jackson-provider for %{name}

%description    jackson-provider
%{extdesc} %{summary}.

%package        jaxb-provider
Summary:        Module jaxb-provider for %{name}

%description    jaxb-provider
%{extdesc} %{summary}.

%package        jaxrs
Summary:        Module jaxrs for %{name}

%description    jaxrs
%{extdesc} %{summary}.

%package        jaxrs-all
Summary:        Module jaxrs-all for %{name}

%description    jaxrs-all
%{extdesc} %{summary}.

%package        jettison-provider
Summary:        Module jettison-provider for %{name}

%description    jettison-provider
%{extdesc} %{summary}.

%package        tjws
Summary:        Module tjws for %{name}

%description    tjws
%{extdesc} %{summary}.

%package	client
Summary: 	Client for %{name}

%description    client
%{extdesc} %{summary}.

%package        resteasy-pom
Summary:        Module pom for %{name}

%description    resteasy-pom
%{extdesc} %{summary}.

%prep
%setup -q -n Resteasy-%{namedversion}

# Disable unnecesary modules
%pom_disable_module examples jaxrs/pom.xml
%pom_disable_module profiling-tests jaxrs/pom.xml
%pom_disable_module resteasy-test-data jaxrs/pom.xml
%pom_disable_module war-tests jaxrs/pom.xml
%pom_disable_module resteasy-links jaxrs/pom.xml
%pom_disable_module jboss-modules jaxrs/pom.xml

%pom_disable_module resteasy-cache jaxrs/pom.xml
%pom_disable_module security jaxrs/pom.xml
%pom_disable_module resteasy-spring jaxrs/pom.xml
%pom_disable_module resteasy-bom jaxrs/pom.xml
%pom_disable_module resteasy-guice jaxrs/pom.xml
%pom_disable_module resteasy-jsapi jaxrs/pom.xml
%pom_disable_module async-http-servlet-3.0 jaxrs/pom.xml
%pom_disable_module resteasy-cdi jaxrs/pom.xml
%pom_disable_module server-adapters jaxrs/pom.xml
%pom_disable_module resteasy-jaxrs-testsuite jaxrs/pom.xml
%pom_disable_module resteasy-servlet-initializer jaxrs/pom.xml

%pom_disable_module resteasy-oauth jaxrs/security/pom.xml
%pom_disable_module login-module-authenticator jaxrs/security/pom.xml
%pom_disable_module skeleton-key-idm jaxrs/security/pom.xml
%pom_disable_module keystone/keystone-as7 jaxrs/security/pom.xml
%pom_disable_module keystone/keystone-as7-modules jaxrs/security/pom.xml

%pom_disable_module async-http-servlet-3.0-test jaxrs/async-http-servlet-3.0/pom.xml
%pom_disable_module callback-test jaxrs/async-http-servlet-3.0/pom.xml

%pom_disable_module fastinfoset jaxrs/providers/pom.xml
%pom_disable_module multipart jaxrs/providers/pom.xml
%pom_disable_module yaml jaxrs/providers/pom.xml
%pom_disable_module resteasy-html jaxrs/providers/pom.xml
%pom_disable_module test-resteasy-html jaxrs/providers/pom.xml
%pom_disable_module test-all-jaxb jaxrs/providers/pom.xml
%pom_disable_module test-jackson-jaxb-coexistence jaxrs/providers/pom.xml
%pom_disable_module resteasy-hibernatevalidator-provider jaxrs/providers/pom.xml
%pom_disable_module jackson2 jaxrs/providers/pom.xml
%pom_disable_module json-p-ee7 jaxrs/providers/pom.xml
%pom_disable_module resteasy-validator-provider-11 jaxrs/providers/pom.xml

# Leave Netty 3, disable Netty 4
%pom_disable_module resteasy-netty4 jaxrs/server-adapters/pom.xml

# Replace 2.5 servlet with the jboss-servlet-2.5-api provides
for m in jaxrs/tjws; do
%pom_remove_dep "javax.servlet:servlet-api" ${m}/pom.xml
%pom_add_dep "org.jboss.spec.javax.servlet:jboss-servlet-api_2.5_spec" ${m}/pom.xml
done

# Need to be patched to work with Jetty 9
rm jaxrs/resteasy-spring/src/main/java/org/jboss/resteasy/springmvc/JettyLifecycleManager.java

%pom_remove_dep "org.springframework:spring-test" jaxrs/resteasy-spring/pom.xml
%pom_remove_dep "org.mortbay.jetty:jetty" jaxrs/resteasy-spring/pom.xml
%pom_add_dep "org.eclipse.jetty:jetty-server" jaxrs/resteasy-spring/pom.xml
%pom_remove_dep net.jcip:jcip-annotations jaxrs/pom.xml
%pom_remove_dep net.jcip:jcip-annotations jaxrs/resteasy-jaxrs/pom.xml
%pom_remove_plugin com.atlassian.maven.plugins:maven-clover2-plugin jaxrs/pom.xml
%pom_remove_plugin com.atlassian.maven.plugins:maven-clover2-plugin jaxrs/resteasy-jaxrs/pom.xml

# Fixing JDK7 ASCII issues
files='
jaxrs/resteasy-jsapi/src/main/java/org/jboss/resteasy/jsapi/JSAPIWriter.java
jaxrs/resteasy-jsapi/src/main/java/org/jboss/resteasy/jsapi/JSAPIServlet.java
jaxrs/resteasy-jsapi/src/main/java/org/jboss/resteasy/jsapi/ServiceRegistry.java
jaxrs/providers/jaxb/src/main/java/org/jboss/resteasy/plugins/providers/jaxb/ExternalEntityUnmarshaller.java
'

for f in ${files}; do
native2ascii -encoding UTF8 ${f} ${f}
done

%patch0 -p1
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

# additional gId:aId for jaxrs-api
%mvn_alias ":jaxrs-api" "org.jboss.spec.javax.ws.rs:jboss-jaxrs-api_1.1_spec"

%build
# build, skip tests, singleton packaging
%mvn_build -f -s

# Create Jandex index file(s)
# Not all files are required by JBoss AS7, but let's create indexes for all of them
find -name 'resteasy-*-%{namedversion}.jar' | while read f; do
  java -cp $(build-classpath jandex) org.jboss.jandex.Main -j ${f}
done

%install
%mvn_install

find -name "resteasy-*-jandex.jar" | while read f; do
  install -pm 644 ${f} %{buildroot}%{_javadir}/%{name}/$(basename -s "-%{namedversion}-jandex.jar" $f)-jandex.jar
done

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc jaxrs/License.html jaxrs/README.html
%files jaxrs-all -f .mfiles-resteasy-jaxrs-all
%files providers-pom -f .mfiles-providers-pom
%files jaxrs-api -f .mfiles-jaxrs-api
%files atom-provider -f .mfiles-resteasy-atom-provider
%{_javadir}/%{name}/resteasy-atom-provider-jandex.jar
%files jackson-provider -f .mfiles-resteasy-jackson-provider
%{_javadir}/%{name}/resteasy-jackson-provider-jandex.jar
%files jaxb-provider -f .mfiles-resteasy-jaxb-provider
%{_javadir}/%{name}/resteasy-jaxb-provider-jandex.jar
%files jaxrs -f .mfiles-resteasy-jaxrs
%{_javadir}/%{name}/resteasy-jaxrs-jandex.jar
%files jettison-provider -f .mfiles-resteasy-jettison-provider
%{_javadir}/%{name}/resteasy-jettison-provider-jandex.jar
%files tjws -f .mfiles-tjws
%files javadoc -f .mfiles-javadoc
%doc jaxrs/License.html
%files client -f .mfiles-resteasy-client
%{_javadir}/%{name}/resteasy-client-jandex.jar
%files resteasy-pom -f .mfiles-resteasy-pom


%changelog
* Mon Sep 26 2016 Ade Lee <alee@redhat.com> - 3.0.6-4
- Resolves: rhbz1378619 - disable SerializerProvider by default 

* Thu Jul 28 2016 Ade Lee <alee@redhat.com> - 3.0.6-3
- Resolves: rhbz1357624 - fail to build with java 8

* Fri Jun 24 2016 Ade Lee <alee@redhat.com> - 3.0.6-2
- Resolves: rhbz1280539 - fix pom version

* Sun Sep 7 2014 Ade Lee <alee@redhat.com> - 3.0.6-1
- Resolves: rhbz1139067 - rebase to 3.0.6

* Mon Aug 25 2014 Ade Lee <alee@redhat.com> - 2.3.5-3
- Resolves: rhbz1121918 -  CVE-2014-3490: XXE via parameter entities

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.3.5-2
- Mass rebuild 2013-12-27

* Thu Oct 24 2013 Ade Lee <alee@redhat.com> - 2.3.5-1
- Resolved Bugzilla #1017459 - resteasy-base contains known vulnerable components

* Tue Jul 2 2013 Ade Lee <alee@redhat.com> - 2.3.2-12
- Removed modules not needed for pki-core
- Bugzilla # 973224 - resteasy-base must be split into subpackages to 
  simplify dependencies.  With help from msrb.

* Thu May 9 2013 Ade Lee <alee@redhat.com> - 2.3.2-11
- Removed unneeded maven-checkstyle-plugin BR
- Removed Tomcat 6 dependency
- Replaced maven BR with maven-local

* Fri Jan 4 2013 Ade Lee <alee@redhat.com> - 2.3.2-10
- Disabled resteasy-cdi for rhel 7.0

* Tue Aug 7 2012 Ade Lee <alee@redhat.com> - 2.3.2-9
- Added tomcat6-servlet-2.5-api as a dependency

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr 24 2012 Marek Goldmann <mgoldman@redhat.com> 2.3.2-7
- Create also the jandex index jar files

* Tue Apr 24 2012 Marek Goldmann <mgoldman@redhat.com> 2.3.2-6
- Added resteasy-multipart-provider module

* Mon Apr 23 2012 Juan Hernandez <juan.hernandez@redhat.com> 2.3.2-5
- Fix the async HTTP Servlet 3.0 artifact id

* Mon Apr 23 2012 Juan Hernandez <juan.hernandez@redhat.com> 2.3.2-4
- Added an additional artifact and group id for jaxrs-api

* Mon Apr 23 2012 Juan Hernandez <juan.hernandez@redhat.com> 2.3.2-3
- Added async HTTP Servlet 3.0 module

* Thu Apr 12 2012 Juan Hernandez <juan.hernandez@redhat.com> 2.3.2-2
- Build CDI integration module (bug #812978)

* Tue Mar 6 2012 Ade Lee <alee@redhat.com> 2.3.2-1
- Initial packaging
