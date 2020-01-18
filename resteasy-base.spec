%global namedreltag .Final
%global namedversion %{version}%{namedreltag}
%global prodname resteasy

Name:           resteasy-base
Version:        2.3.5
Release:        1%{?dist}
Summary:        Framework for RESTful Web services and Java applications
License:        ASL 2.0 and CDDL
URL:            http://www.jboss.org/resteasy

# git clone git://github.com/resteasy/Resteasy.git
# cd Resteasy
# git archive --prefix=resteasy-2.3.5.Final/ --output=resteasy-2.3.5.Final.tgz 2.3.5.Final
Source0:        %{prodname}-%{namedversion}.tgz

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


%prep
%setup -q -n %{prodname}-%{namedversion}

# remove unneeded modules
%pom_disable_module resteasy-jaxrs-war
%pom_disable_module resteasy-cache
%pom_disable_module eagledns
%pom_disable_module security
%pom_disable_module resteasy-links
%pom_disable_module arquillian
%pom_disable_module async-http-jbossweb
%pom_disable_module async-http-tomcat
%pom_disable_module resteasy-spring
%pom_disable_module war-tests
%pom_disable_module examples
%pom_disable_module profiling-tests
%pom_disable_module resteasy-test-data
%pom_disable_module resteasy-bom
%pom_disable_module resteasy-guice
%pom_disable_module resteasy-jsapi
%pom_disable_module async-http-servlet-3.0
%pom_disable_module resteasy-cdi
%pom_disable_module jboss-modules
%pom_disable_module server-adapters

%pom_disable_module fastinfoset providers
%pom_disable_module multipart providers
%pom_disable_module yaml providers
%pom_disable_module resteasy-html providers
%pom_disable_module test-resteasy-html providers
%pom_disable_module test-all-jaxb providers
%pom_disable_module test-jackson-jaxb-coexistence providers
%pom_disable_module resteasy-hibernatevalidator-provider providers

%pom_remove_dep net.jcip:jcip-annotations
%pom_remove_dep net.jcip:jcip-annotations resteasy-jaxrs

%pom_remove_plugin com.atlassian.maven.plugins:maven-clover2-plugin
%pom_remove_plugin com.atlassian.maven.plugins:maven-clover2-plugin resteasy-jaxrs

# Fix gId:aId javax.servlet:servlet-api ->
# org.jboss.spec.javax.servlet:jboss-servlet-api_2.5_spec
# in resteasy-jaxrs/pom.xml:
%pom_xpath_replace "pom:dependency[pom:artifactId[text()='servlet-api']]" \
  "<dependency>
     <groupId>org.jboss.spec.javax.servlet</groupId>
     <artifactId>jboss-servlet-api_2.5_spec</artifactId>
     <scope>provided</scope>
   </dependency>" resteasy-jaxrs
# in tjws/pom.xml:
%pom_xpath_replace "pom:dependency[pom:artifactId[text()='servlet-api']]" \
  "<dependency>
     <groupId>org.jboss.spec.javax.servlet</groupId>
     <artifactId>jboss-servlet-api_2.5_spec</artifactId>
     <scope>provided</scope>
   </dependency>" tjws


# additional gId:aId for jaxrs-api
%mvn_alias ":jaxrs-api" "org.jboss.spec.javax.ws.rs:jboss-jaxrs-api_1.1_spec"

%build
# build, skip tests, singleton packaging
%mvn_build -f -s

%install
# Install jars, poms and dependencies maps
%mvn_install

# Create also the Jandex index files
# Required by JBoss AS7
while read module_path artifact_id additional_aid_gid
do
  base_name=${module_path}/target/${artifact_id}-%{namedversion}
  jandex_file=${base_name}-jandex.jar
  if [ -f ${base_name}.jar ]; then
    java -cp $(build-classpath jandex) org.jboss.jandex.Main -j ${base_name}.jar
    install -pm 644 ${jandex_file} %{buildroot}%{_javadir}/%{name}/${artifact_id}-jandex.jar
  fi
done <<'.'
. jaxrs-all
jaxrs-api jaxrs-api org.jboss.spec.javax.ws.rs:jboss-jaxrs-api_1.1_spec
providers/jackson resteasy-jackson-provider
providers/jaxb resteasy-jaxb-provider
providers/jettison resteasy-jettison-provider
providers/resteasy-atom resteasy-atom-provider
resteasy-jaxrs resteasy-jaxrs
tjws tjws
.


%files -f .mfiles
%dir %{_javadir}/%{name}
%doc License.html README.html
%files jaxrs-all -f .mfiles-resteasy-jaxrs-all
%files providers-pom -f .mfiles-providers-pom
%files jaxrs-api -f .mfiles-jaxrs-api
%{_javadir}/%{name}/jaxrs-api-jandex.jar
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
%{_javadir}/%{name}/tjws-jandex.jar
%files javadoc -f .mfiles-javadoc
%doc License.html


%changelog
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
