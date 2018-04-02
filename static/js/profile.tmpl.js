(function() {
  var template = Handlebars.template, templates = Handlebars.templates = Handlebars.templates || {};
templates['profile.tmpl'] = template({"1":function(container,depth0,helpers,partials,data) {
    return "       <div class=\"col-sm-8\">\n";
},"3":function(container,depth0,helpers,partials,data) {
    return "       <div class=\"col-sm-12\">\n";
},"5":function(container,depth0,helpers,partials,data) {
    return container.escapeExpression((helpers.Hsex || (depth0 && depth0.Hsex) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.victim_sex : depth0),{"name":"Hsex","hash":{},"data":data}));
},"7":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = (helpers.ifKnown || (depth0 && depth0.ifKnown) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.victim_age : depth0),{"name":"ifKnown","hash":{},"fn":container.program(8, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"8":function(container,depth0,helpers,partials,data) {
    var stack1, helper, alias1=depth0 != null ? depth0 : (container.nullContext || {});

  return ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.victim_sex : depth0),{"name":"if","hash":{},"fn":container.program(9, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "        \n      age "
    + container.escapeExpression(((helper = (helper = helpers.victim_age || (depth0 != null ? depth0.victim_age : depth0)) != null ? helper : helpers.helperMissing),(typeof helper === "function" ? helper.call(alias1,{"name":"victim_age","hash":{},"data":data}) : helper)))
    + "        \n"
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.victim_disappeared_killed : depth0),{"name":"if","hash":{},"fn":container.program(11, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "      ";
},"9":function(container,depth0,helpers,partials,data) {
    return ",";
},"11":function(container,depth0,helpers,partials,data) {
    var stack1, alias1=depth0 != null ? depth0 : (container.nullContext || {}), alias2=helpers.helperMissing;

  return "         at time of \n"
    + ((stack1 = (helpers.equal || (depth0 && depth0.equal) || alias2).call(alias1,(depth0 != null ? depth0.victim_disappeared_killed : depth0),1,{"name":"equal","hash":{},"fn":container.program(12, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + ((stack1 = (helpers.equal || (depth0 && depth0.equal) || alias2).call(alias1,(depth0 != null ? depth0.victim_disappeared_killed : depth0),2,{"name":"equal","hash":{},"fn":container.program(14, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"12":function(container,depth0,helpers,partials,data) {
    return "          disappearance\n";
},"14":function(container,depth0,helpers,partials,data) {
    return "          killing\n";
},"16":function(container,depth0,helpers,partials,data) {
    return "        <p>Killed"
    + container.escapeExpression((helpers.Hdate || (depth0 && depth0.Hdate) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.victim_death_date : depth0),{"name":"Hdate","hash":{},"data":data}))
    + "</p>\n";
},"18":function(container,depth0,helpers,partials,data) {
    var stack1, alias1=depth0 != null ? depth0 : (container.nullContext || {}), alias2=helpers.helperMissing;

  return "        <p>Disappeared"
    + ((stack1 = (helpers.equal || (depth0 && depth0.equal) || alias2).call(alias1,(depth0 != null ? depth0.victim_last_heard_alive : depth0),4,{"name":"equal","hash":{},"fn":container.program(19, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + ((stack1 = (helpers.equal || (depth0 && depth0.equal) || alias2).call(alias1,(depth0 != null ? depth0.victim_last_heard_alive : depth0),1,{"name":"equal","hash":{},"fn":container.program(21, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + ((stack1 = (helpers.equal || (depth0 && depth0.equal) || alias2).call(alias1,(depth0 != null ? depth0.victim_last_heard_alive : depth0),2,{"name":"equal","hash":{},"fn":container.program(23, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + ((stack1 = (helpers.equal || (depth0 && depth0.equal) || alias2).call(alias1,(depth0 != null ? depth0.victim_last_heard_alive : depth0),3,{"name":"equal","hash":{},"fn":container.program(25, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "</p>\n";
},"19":function(container,depth0,helpers,partials,data) {
    return ", date unknown";
},"21":function(container,depth0,helpers,partials,data) {
    return container.escapeExpression((helpers.Hdate || (depth0 && depth0.Hdate) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.victim_arrest_date : depth0),{"name":"Hdate","hash":{},"data":data}));
},"23":function(container,depth0,helpers,partials,data) {
    return container.escapeExpression((helpers.Hdate || (depth0 && depth0.Hdate) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.victim_death_date : depth0),{"name":"Hdate","hash":{},"data":data}));
},"25":function(container,depth0,helpers,partials,data) {
    return container.escapeExpression((helpers.Hdate || (depth0 && depth0.Hdate) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.dt_last_heard_victim_alive : depth0),{"name":"Hdate","hash":{},"data":data}));
},"27":function(container,depth0,helpers,partials,data) {
    var stack1;

  return "\n"
    + ((stack1 = helpers["if"].call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.village_name : depth0),{"name":"if","hash":{},"fn":container.program(28, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n";
},"28":function(container,depth0,helpers,partials,data) {
    var helper;

  return "          <div class=\"row\">  \n            <div class=\"col-sm-2\">\n              <p class=\"kicker\">Residence</p>\n            </div>\n            <div class=\"col-sm-10\">\n              <p>"
    + container.escapeExpression(((helper = (helper = helpers.village_name || (depth0 != null ? depth0.village_name : depth0)) != null ? helper : helpers.helperMissing),(typeof helper === "function" ? helper.call(depth0 != null ? depth0 : (container.nullContext || {}),{"name":"village_name","hash":{},"data":data}) : helper)))
    + "</p>\n            </div>\n          </div>\n";
},"30":function(container,depth0,helpers,partials,data) {
    var stack1;

  return "\n"
    + ((stack1 = helpers["if"].call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.victim_address_other : depth0),{"name":"if","hash":{},"fn":container.program(31, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"31":function(container,depth0,helpers,partials,data) {
    return "        <div class=\"row\">  \n          <div class=\"col-sm-2\">\n            <p class=\"kicker\">Residence</p>\n          </div>\n          <div class=\"col-sm-10\">\n            <p>"
    + container.escapeExpression((helpers.Hvictim_address_other || (depth0 && depth0.Hvictim_address_other) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.victim_address_other : depth0),{"name":"Hvictim_address_other","hash":{},"data":data}))
    + "</p>\n          </div>\n        </div>\n";
},"33":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.victim_education : depth0),11,{"name":"isnot","hash":{},"fn":container.program(34, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"34":function(container,depth0,helpers,partials,data) {
    return "      <div class=\"row\">  \n        <div class=\"col-sm-2\">\n          <p class=\"kicker\">Education</p>\n        </div>\n        <div class=\"col-sm-10\">\n          <p>"
    + container.escapeExpression((helpers.Heducation || (depth0 && depth0.Heducation) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.victim_education : depth0),{"name":"Heducation","hash":{},"data":data}))
    + "</p>\n        </div>\n      </div>\n";
},"36":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.victim_employment___11 : depth0),1,{"name":"isnot","hash":{},"fn":container.program(37, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"37":function(container,depth0,helpers,partials,data) {
    var stack1;

  return "    \n"
    + ((stack1 = (helpers.ifArray || (depth0 && depth0.ifArray) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.victim_employment___1 : depth0),(depth0 != null ? depth0.victim_employment___2 : depth0),(depth0 != null ? depth0.victim_employment___3 : depth0),(depth0 != null ? depth0.victim_employment___4 : depth0),(depth0 != null ? depth0.victim_employment___5 : depth0),(depth0 != null ? depth0.victim_employment___6 : depth0),(depth0 != null ? depth0.victim_employment___7 : depth0),(depth0 != null ? depth0.victim_employment___8 : depth0),(depth0 != null ? depth0.victim_employment___9 : depth0),(depth0 != null ? depth0.victim_employment___10 : depth0),(depth0 != null ? depth0.victim_employment___11 : depth0),{"name":"ifArray","hash":{},"fn":container.program(38, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n";
},"38":function(container,depth0,helpers,partials,data) {
    return "      <div class=\"row\">  \n      <div class=\"col-sm-2\">\n        <p class=\"kicker\">Employment</p>\n      </div>\n      <div class=\"col-sm-10\">\n        <p>"
    + container.escapeExpression((helpers.Hvictim_employment || (depth0 && depth0.Hvictim_employment) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.victim_employment___1 : depth0),(depth0 != null ? depth0.victim_employment___2 : depth0),(depth0 != null ? depth0.victim_employment___3 : depth0),(depth0 != null ? depth0.victim_employment___4 : depth0),(depth0 != null ? depth0.victim_employment___5 : depth0),(depth0 != null ? depth0.victim_employment___6 : depth0),(depth0 != null ? depth0.victim_employment___7 : depth0),(depth0 != null ? depth0.victim_employment___8 : depth0),(depth0 != null ? depth0.victim_employment___9 : depth0),(depth0 != null ? depth0.victim_employment___10 : depth0),(depth0 != null ? depth0.victim_employment___11 : depth0),(depth0 != null ? depth0.victim_employment_other : depth0),{"name":"Hvictim_employment","hash":{},"data":data}))
    + "</p>\n      </div>\n      </div>\n";
},"40":function(container,depth0,helpers,partials,data) {
    var helper;

  return "      <div class=\"row\">  \n      <div class=\"col-sm-2\">\n        <p class=\"kicker\">Employment</p>\n      </div>\n      <div class=\"col-sm-10\">\n        <p>"
    + container.escapeExpression(((helper = (helper = helpers.victim_employment_other || (depth0 != null ? depth0.victim_employment_other : depth0)) != null ? helper : helpers.helperMissing),(typeof helper === "function" ? helper.call(depth0 != null ? depth0 : (container.nullContext || {}),{"name":"victim_employment_other","hash":{},"data":data}) : helper)))
    + "</p>\n      </div>\n      </div>\n";
},"42":function(container,depth0,helpers,partials,data) {
    var stack1, alias1=depth0 != null ? depth0 : (container.nullContext || {}), alias2=helpers.helperMissing;

  return "      <div class=\"row\">  \n      <div class=\"col-sm-2\">\n        <p class=\"kicker\">Married</p>\n      </div>\n      <div class=\"col-sm-10\">\n        <p>"
    + container.escapeExpression((helpers.Hyes_no || (depth0 && depth0.Hyes_no) || alias2).call(alias1,(depth0 != null ? depth0.victim_marital_status : depth0),{"name":"Hyes_no","hash":{},"data":data}))
    + "</p>\n      </div>\n      </div>\n    \n"
    + ((stack1 = (helpers.equal || (depth0 && depth0.equal) || alias2).call(alias1,(depth0 != null ? depth0.victim_marital_status : depth0),1,{"name":"equal","hash":{},"fn":container.program(43, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "    \n";
},"43":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = helpers["if"].call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.victim_children : depth0),{"name":"if","hash":{},"fn":container.program(44, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"44":function(container,depth0,helpers,partials,data) {
    var helper;

  return "      <div class=\"row\">  \n        <div class=\"col-sm-2\">\n          <p class=\"kicker\">Children</p>\n        </div>\n        <div class=\"col-sm-10\">\n          <p>"
    + container.escapeExpression(((helper = (helper = helpers.victim_children || (depth0 != null ? depth0.victim_children : depth0)) != null ? helper : helpers.helperMissing),(typeof helper === "function" ? helper.call(depth0 != null ? depth0 : (container.nullContext || {}),{"name":"victim_children","hash":{},"data":data}) : helper)))
    + "</p>\n        </div>\n        </div>\n";
},"46":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.victim_religion : depth0),7,{"name":"isnot","hash":{},"fn":container.program(47, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"47":function(container,depth0,helpers,partials,data) {
    var stack1, alias1=depth0 != null ? depth0 : (container.nullContext || {}), alias2=helpers.helperMissing;

  return "      <div class=\"row\">  \n      <div class=\"col-sm-2\">\n        <p class=\"kicker\">Religion</p>\n      </div>\n      <div class=\"col-sm-10\">\n        <p>"
    + container.escapeExpression((helpers.Hreligion || (depth0 && depth0.Hreligion) || alias2).call(alias1,(depth0 != null ? depth0.victim_religion : depth0),{"name":"Hreligion","hash":{},"data":data}))
    + ((stack1 = (helpers.equal || (depth0 && depth0.equal) || alias2).call(alias1,(depth0 != null ? depth0.victim_amritdhari : depth0),1,{"name":"equal","hash":{},"fn":container.program(48, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + ((stack1 = (helpers.equal || (depth0 && depth0.equal) || alias2).call(alias1,(depth0 != null ? depth0.victim_kesdhari : depth0),1,{"name":"equal","hash":{},"fn":container.program(50, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n        </p>\n      </div>\n      </div>\n";
},"48":function(container,depth0,helpers,partials,data) {
    return ", Amritdhari";
},"50":function(container,depth0,helpers,partials,data) {
    return ", Kesdhari";
},"52":function(container,depth0,helpers,partials,data) {
    var helper;

  return "      <div class=\"row\">  \n      <div class=\"col-sm-2\">\n        <p class=\"kicker\">Religion</p>\n      </div>\n      <div class=\"col-sm-10\">\n        <p>"
    + container.escapeExpression(((helper = (helper = helpers.victim_religion_other || (depth0 != null ? depth0.victim_religion_other : depth0)) != null ? helper : helpers.helperMissing),(typeof helper === "function" ? helper.call(depth0 != null ? depth0 : (container.nullContext || {}),{"name":"victim_religion_other","hash":{},"data":data}) : helper)))
    + "\n        </p>\n      </div>\n      </div>\n";
},"54":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.victim_caste : depth0),9,{"name":"isnot","hash":{},"fn":container.program(55, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"55":function(container,depth0,helpers,partials,data) {
    return "      <div class=\"row\">  \n      <div class=\"col-sm-2\">\n        <p class=\"kicker\">Caste</p>\n      </div>\n      <div class=\"col-sm-10\">\n        <p>"
    + container.escapeExpression((helpers.Hcaste || (depth0 && depth0.Hcaste) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.victim_caste : depth0),{"name":"Hcaste","hash":{},"data":data}))
    + "</p>\n      </div>\n      </div>\n\n";
},"57":function(container,depth0,helpers,partials,data) {
    var helper;

  return "      <div class=\"row\">  \n      <div class=\"col-sm-2\">\n        <p class=\"kicker\">Date of birth</p>\n      </div>\n      <div class=\"col-sm-10\">\n        <p>"
    + container.escapeExpression(((helper = (helper = helpers.victim_dob || (depth0 != null ? depth0.victim_dob : depth0)) != null ? helper : helpers.helperMissing),(typeof helper === "function" ? helper.call(depth0 != null ? depth0 : (container.nullContext || {}),{"name":"victim_dob","hash":{},"data":data}) : helper)))
    + "</p>\n      </div>\n      </div>\n";
},"59":function(container,depth0,helpers,partials,data) {
    var stack1;

  return "      <div class=\"col-sm-4 photos\" >\n        <br>\n        "
    + ((stack1 = (helpers.Hphoto || (depth0 && depth0.Hphoto) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.photo_vic_fn : depth0),{"name":"Hphoto","hash":{},"data":data})) != null ? stack1 : "")
    + "\n      </div>\n";
},"61":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.victim_militant_reason___8 : depth0),1,{"name":"isnot","hash":{},"fn":container.program(62, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"62":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.victim_militant_reason___9 : depth0),1,{"name":"isnot","hash":{},"fn":container.program(63, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"63":function(container,depth0,helpers,partials,data) {
    var stack1;

  return "\n"
    + ((stack1 = (helpers.ifArray || (depth0 && depth0.ifArray) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.victim_militant_reason___1 : depth0),(depth0 != null ? depth0.victim_militant_reason___2 : depth0),(depth0 != null ? depth0.victim_militant_reason___3 : depth0),(depth0 != null ? depth0.victim_militant_reason___4 : depth0),(depth0 != null ? depth0.victim_militant_reason___5 : depth0),(depth0 != null ? depth0.victim_militant_reason___6 : depth0),{"name":"ifArray","hash":{},"fn":container.program(64, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n";
},"64":function(container,depth0,helpers,partials,data) {
    return "    <div class=\"col-sm-6\">\n      <p class=\"kicker\">Reason(s) for joining militancy</p>\n    </div>\n    <div class=\"col-sm-6\">\n      <p>"
    + container.escapeExpression((helpers.Hvictim_militant_reason || (depth0 && depth0.Hvictim_militant_reason) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.victim_militant_reason___1 : depth0),(depth0 != null ? depth0.victim_militant_reason___2 : depth0),(depth0 != null ? depth0.victim_militant_reason___3 : depth0),(depth0 != null ? depth0.victim_militant_reason___4 : depth0),(depth0 != null ? depth0.victim_militant_reason___5 : depth0),(depth0 != null ? depth0.victim_militant_reason___6 : depth0),(depth0 != null ? depth0.victim_militant_reason___7 : depth0),(depth0 != null ? depth0.victim_militant_reason___8 : depth0),(depth0 != null ? depth0.victim_militant_reason_oth : depth0),{"name":"Hvictim_militant_reason","hash":{},"data":data}))
    + "</p>\n    </div>\n";
},"66":function(container,depth0,helpers,partials,data) {
    var helper;

  return "    <div class=\"col-sm-6\">\n      <p class=\"kicker\">Reason(s) for joining militancy</p>\n    </div>\n    <div class=\"col-sm-6\">\n      <p>"
    + container.escapeExpression(((helper = (helper = helpers.victim_militant_reason_oth || (depth0 != null ? depth0.victim_militant_reason_oth : depth0)) != null ? helper : helpers.helperMissing),(typeof helper === "function" ? helper.call(depth0 != null ? depth0 : (container.nullContext || {}),{"name":"victim_militant_reason_oth","hash":{},"data":data}) : helper)))
    + "</p>\n    </div>\n";
},"68":function(container,depth0,helpers,partials,data) {
    var stack1, alias1=depth0 != null ? depth0 : (container.nullContext || {});

  return "    <div class=\"col-sm-6\">\n      <p class=\"kicker\">Militant support provided</p>\n    </div>\n    <div class=\"col-sm-6\">\n      <p>"
    + container.escapeExpression((helpers.Hyes_no || (depth0 && depth0.Hyes_no) || helpers.helperMissing).call(alias1,(depth0 != null ? depth0.victim_militant_support : depth0),{"name":"Hyes_no","hash":{},"data":data}))
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.victim_militant_sprt_vol : depth0),{"name":"if","hash":{},"fn":container.program(69, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "</p>\n    </div>\n";
},"69":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.victim_militant_sprt_vol : depth0),3,{"name":"isnot","hash":{},"fn":container.program(70, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"70":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.victim_militant_sprt_vol : depth0),9,{"name":"isnot","hash":{},"fn":container.program(71, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"71":function(container,depth0,helpers,partials,data) {
    return ", "
    + container.escapeExpression((helpers.Hforced || (depth0 && depth0.Hforced) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.victim_militant_sprt_vol : depth0),{"name":"Hforced","hash":{},"data":data}));
},"73":function(container,depth0,helpers,partials,data) {
    var stack1, alias1=depth0 != null ? depth0 : (container.nullContext || {}), alias2=helpers.helperMissing;

  return "    <div class=\"col-sm-6\">\n      <p class=\"kicker\">Prior detentions</p>\n    </div>\n    <div class=\"col-sm-6\">\n      <p>"
    + container.escapeExpression((helpers.Hyes_no || (depth0 && depth0.Hyes_no) || alias2).call(alias1,(depth0 != null ? depth0.victim_prior_detention_st : depth0),{"name":"Hyes_no","hash":{},"data":data}))
    + ((stack1 = (helpers.ifKnown || (depth0 && depth0.ifKnown) || alias2).call(alias1,(depth0 != null ? depth0.victim_prior_detentions : depth0),{"name":"ifKnown","hash":{},"fn":container.program(74, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "</p>\n    </div>\n";
},"74":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = (helpers.equal || (depth0 && depth0.equal) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.victim_prior_detention_st : depth0),1,{"name":"equal","hash":{},"fn":container.program(75, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"75":function(container,depth0,helpers,partials,data) {
    var helper;

  return ", "
    + container.escapeExpression(((helper = (helper = helpers.victim_prior_detentions || (depth0 != null ? depth0.victim_prior_detentions : depth0)) != null ? helper : helpers.helperMissing),(typeof helper === "function" ? helper.call(depth0 != null ? depth0 : (container.nullContext || {}),{"name":"victim_prior_detentions","hash":{},"data":data}) : helper)));
},"77":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.victim_prior_detention_trt : depth0),9,{"name":"isnot","hash":{},"fn":container.program(78, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"78":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = (helpers.equal || (depth0 && depth0.equal) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.victim_prior_detention_st : depth0),1,{"name":"equal","hash":{},"fn":container.program(79, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"79":function(container,depth0,helpers,partials,data) {
    return "    <div class=\"col-sm-6\">\n      <p class=\"kicker\">Prior torture</p>\n    </div>\n    <div class=\"col-sm-6\">\n      <p>"
    + container.escapeExpression((helpers.Hyes_no_na || (depth0 && depth0.Hyes_no_na) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.victim_prior_detention_trt : depth0),{"name":"Hyes_no_na","hash":{},"data":data}))
    + "</p>\n    </div>\n";
},"81":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.target_reason___9 : depth0),1,{"name":"isnot","hash":{},"fn":container.program(82, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"82":function(container,depth0,helpers,partials,data) {
    var stack1;

  return "\n"
    + ((stack1 = (helpers.ifArray || (depth0 && depth0.ifArray) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.target_reason___1 : depth0),(depth0 != null ? depth0.target_reason___2 : depth0),(depth0 != null ? depth0.target_reason___3 : depth0),(depth0 != null ? depth0.target_reason___4 : depth0),(depth0 != null ? depth0.target_reason___5 : depth0),(depth0 != null ? depth0.target_reason___6 : depth0),(depth0 != null ? depth0.target_reason___7 : depth0),(depth0 != null ? depth0.target_reason___8 : depth0),(depth0 != null ? depth0.target_reason___9 : depth0),{"name":"ifArray","hash":{},"fn":container.program(83, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n";
},"83":function(container,depth0,helpers,partials,data) {
    return "    <div class=\"col-sm-6\">\n      <p class=\"kicker\">Perceived reason for targeting victim</p>\n    </div>\n    <div class=\"col-sm-6\">\n      <p>"
    + container.escapeExpression((helpers.Htarget_reason || (depth0 && depth0.Htarget_reason) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.target_reason___1 : depth0),(depth0 != null ? depth0.target_reason___2 : depth0),(depth0 != null ? depth0.target_reason___3 : depth0),(depth0 != null ? depth0.target_reason___4 : depth0),(depth0 != null ? depth0.target_reason___5 : depth0),(depth0 != null ? depth0.target_reason___6 : depth0),(depth0 != null ? depth0.target_reason___7 : depth0),(depth0 != null ? depth0.target_reason___8 : depth0),(depth0 != null ? depth0.target_reason___9 : depth0),(depth0 != null ? depth0.target_reason_other : depth0),{"name":"Htarget_reason","hash":{},"data":data}))
    + "</p>\n    </div>\n";
},"85":function(container,depth0,helpers,partials,data) {
    var helper;

  return "    <div class=\"col-sm-6\">\n      <p class=\"kicker\">Perceived reason for targeting victim</p>\n    </div>\n    <div class=\"col-sm-6\">\n      <p>"
    + container.escapeExpression(((helper = (helper = helpers.target_reason_other || (depth0 != null ? depth0.target_reason_other : depth0)) != null ? helper : helpers.helperMissing),(typeof helper === "function" ? helper.call(depth0 != null ? depth0 : (container.nullContext || {}),{"name":"target_reason_other","hash":{},"data":data}) : helper)))
    + "</p>\n    </div>\n";
},"87":function(container,depth0,helpers,partials,data) {
    var stack1, alias1=depth0 != null ? depth0 : (container.nullContext || {});

  return "    <div class=\"col-sm-6\">\n      <p class=\"kicker\">Abduction/arrest prior to killing/disappearance</p>\n    </div>\n    <div class=\"col-sm-6\">\n      <p>"
    + container.escapeExpression((helpers.Hvictim_arrest_status || (depth0 && depth0.Hvictim_arrest_status) || helpers.helperMissing).call(alias1,(depth0 != null ? depth0.victim_arrest_status : depth0),{"name":"Hvictim_arrest_status","hash":{},"data":data}))
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.victim_arrest_date : depth0),{"name":"if","hash":{},"fn":container.program(88, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "</p>\n    </div>\n";
},"88":function(container,depth0,helpers,partials,data) {
    var alias1=depth0 != null ? depth0 : (container.nullContext || {}), alias2=helpers.helperMissing, alias3=container.escapeExpression;

  return ", "
    + alias3((helpers.Hvictim_arrest_date || (depth0 && depth0.Hvictim_arrest_date) || alias2).call(alias1,(depth0 != null ? depth0.victim_arrest_exact_date : depth0),(depth0 != null ? depth0.victim_arrest_date : depth0),{"name":"Hvictim_arrest_date","hash":{},"data":data}))
    + alias3((helpers.Hdate_no_on || (depth0 && depth0.Hdate_no_on) || alias2).call(alias1,(depth0 != null ? depth0.victim_arrest_date : depth0),{"name":"Hdate_no_on","hash":{},"data":data}));
},"90":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.victim_arrest_location : depth0),11,{"name":"isnot","hash":{},"fn":container.program(91, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"91":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = (helpers.equalor || (depth0 && depth0.equalor) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.victim_arrest_status : depth0),2,(depth0 != null ? depth0.victim_arrest_status : depth0),1,{"name":"equalor","hash":{},"fn":container.program(92, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"92":function(container,depth0,helpers,partials,data) {
    var stack1, alias1=depth0 != null ? depth0 : (container.nullContext || {});

  return "      <div class=\"col-sm-6\">\n        <p class=\"kicker\">Place of abduction/arrest</p>\n      </div>\n      <div class=\"col-sm-6\">\n        <p>"
    + container.escapeExpression((helpers.Hvictim_arrest_location || (depth0 && depth0.Hvictim_arrest_location) || helpers.helperMissing).call(alias1,(depth0 != null ? depth0.victim_arrest_location : depth0),{"name":"Hvictim_arrest_location","hash":{},"data":data}))
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.victim_arrest_loc_vill : depth0),{"name":"if","hash":{},"fn":container.program(93, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.victim_arrest_loc_thsl : depth0),{"name":"if","hash":{},"fn":container.program(95, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.victim_arrest_loc_dist : depth0),{"name":"if","hash":{},"fn":container.program(97, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.victim_arrest_loc_st : depth0),{"name":"if","hash":{},"fn":container.program(99, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "</p>\n      </div>\n";
},"93":function(container,depth0,helpers,partials,data) {
    var helper;

  return container.escapeExpression(((helper = (helper = helpers.victim_arrest_loc_vill || (depth0 != null ? depth0.victim_arrest_loc_vill : depth0)) != null ? helper : helpers.helperMissing),(typeof helper === "function" ? helper.call(depth0 != null ? depth0 : (container.nullContext || {}),{"name":"victim_arrest_loc_vill","hash":{},"data":data}) : helper)));
},"95":function(container,depth0,helpers,partials,data) {
    var helper;

  return ", \n"
    + container.escapeExpression(((helper = (helper = helpers.victim_arrest_loc_thsl || (depth0 != null ? depth0.victim_arrest_loc_thsl : depth0)) != null ? helper : helpers.helperMissing),(typeof helper === "function" ? helper.call(depth0 != null ? depth0 : (container.nullContext || {}),{"name":"victim_arrest_loc_thsl","hash":{},"data":data}) : helper)));
},"97":function(container,depth0,helpers,partials,data) {
    var helper;

  return ", \n"
    + container.escapeExpression(((helper = (helper = helpers.victim_arrest_loc_dist || (depth0 != null ? depth0.victim_arrest_loc_dist : depth0)) != null ? helper : helpers.helperMissing),(typeof helper === "function" ? helper.call(depth0 != null ? depth0 : (container.nullContext || {}),{"name":"victim_arrest_loc_dist","hash":{},"data":data}) : helper)));
},"99":function(container,depth0,helpers,partials,data) {
    var helper;

  return ", \n"
    + container.escapeExpression(((helper = (helper = helpers.victim_arrest_loc_st || (depth0 != null ? depth0.victim_arrest_loc_st : depth0)) != null ? helper : helpers.helperMissing),(typeof helper === "function" ? helper.call(depth0 != null ? depth0 : (container.nullContext || {}),{"name":"victim_arrest_loc_st","hash":{},"data":data}) : helper)));
},"101":function(container,depth0,helpers,partials,data) {
    return "    <div class=\"col-sm-6\">\n      <p class=\"kicker\">Witness(es) to abduction/arrest</p>\n    </div>\n    <div class=\"col-sm-6\">      \n        <p>"
    + container.escapeExpression((helpers.Hwitness_arrest || (depth0 && depth0.Hwitness_arrest) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.witness_arrest___0 : depth0),(depth0 != null ? depth0.witness_arrest___1 : depth0),(depth0 != null ? depth0.witness_arrest___2 : depth0),(depth0 != null ? depth0.witness_arrest___3 : depth0),(depth0 != null ? depth0.witness_arrest___4 : depth0),(depth0 != null ? depth0.witness_arrest___5 : depth0),(depth0 != null ? depth0.witness_arrest___6 : depth0),(depth0 != null ? depth0.witness_arrest___7 : depth0),(depth0 != null ? depth0.witness_arrest___8 : depth0),(depth0 != null ? depth0.witness_arrest___9 : depth0),(depth0 != null ? depth0.witness_arrest___10 : depth0),(depth0 != null ? depth0.witness_arrest___12 : depth0),(depth0 != null ? depth0.witness_arrest_oth : depth0),{"name":"Hwitness_arrest","hash":{},"data":data}))
    + "</p>\n    </div>\n";
},"103":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.so_inform_witnesses : depth0),3,{"name":"isnot","hash":{},"fn":container.program(104, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"104":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = helpers["if"].call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.so_inform_witnesses : depth0),{"name":"if","hash":{},"fn":container.program(105, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"105":function(container,depth0,helpers,partials,data) {
    return "    <div class=\"col-sm-6\">\n      <p class=\"kicker\">Security officials informed witnesses about destination</p>\n    </div>\n    <div class=\"col-sm-6\">\n      <p>"
    + container.escapeExpression((helpers.Hyes_no_na || (depth0 && depth0.Hyes_no_na) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.so_inform_witnesses : depth0),{"name":"Hyes_no_na","hash":{},"data":data}))
    + "</p>\n    </div>\n";
},"107":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.security_forces_uniformed : depth0),9,{"name":"isnot","hash":{},"fn":container.program(108, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"108":function(container,depth0,helpers,partials,data) {
    return "    <div class=\"col-sm-6\">\n      <p class=\"kicker\">Uniformed</p>\n    </div>\n    <div class=\"col-sm-6\">\n      <p>"
    + container.escapeExpression((helpers.Hyes_no || (depth0 && depth0.Hyes_no) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.security_forces_uniformed : depth0),{"name":"Hyes_no","hash":{},"data":data}))
    + "</p>\n    </div>\n";
},"110":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.demands___10 : depth0),1,{"name":"isnot","hash":{},"fn":container.program(111, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"111":function(container,depth0,helpers,partials,data) {
    var stack1;

  return "\n    "
    + ((stack1 = (helpers.ifArray || (depth0 && depth0.ifArray) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.demands___1 : depth0),(depth0 != null ? depth0.demands___2 : depth0),(depth0 != null ? depth0.demands___3 : depth0),(depth0 != null ? depth0.demands___4 : depth0),(depth0 != null ? depth0.demands___5 : depth0),(depth0 != null ? depth0.demands___6 : depth0),(depth0 != null ? depth0.demands___7 : depth0),(depth0 != null ? depth0.demands___8 : depth0),(depth0 != null ? depth0.demands___9 : depth0),(depth0 != null ? depth0.demands___10 : depth0),(depth0 != null ? depth0.other_demands : depth0),{"name":"ifArray","hash":{},"fn":container.program(112, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n";
},"112":function(container,depth0,helpers,partials,data) {
    return "</p>\n\n    <div class=\"col-sm-6\">\n      <p class=\"kicker\">Demands by security forces</p>\n    </div>\n    <div class=\"col-sm-6\">\n      <p>"
    + container.escapeExpression((helpers.Hdemands || (depth0 && depth0.Hdemands) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.demands___1 : depth0),(depth0 != null ? depth0.demands___2 : depth0),(depth0 != null ? depth0.demands___3 : depth0),(depth0 != null ? depth0.demands___4 : depth0),(depth0 != null ? depth0.demands___5 : depth0),(depth0 != null ? depth0.demands___6 : depth0),(depth0 != null ? depth0.demands___7 : depth0),(depth0 != null ? depth0.demands___8 : depth0),(depth0 != null ? depth0.demands___9 : depth0),(depth0 != null ? depth0.demands___10 : depth0),(depth0 != null ? depth0.other_demands : depth0),{"name":"Hdemands","hash":{},"data":data}))
    + "</p>\n    </div>\n\n";
},"114":function(container,depth0,helpers,partials,data) {
    return "    <div class=\"col-sm-6\">\n      <p class=\"kicker\">Presented before judge/magistrate</p>\n    </div>\n    <div class=\"col-sm-6\">\n      <p>"
    + container.escapeExpression((helpers.Hyes_no_unknown || (depth0 && depth0.Hyes_no_unknown) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.judge_or_magistrate_status : depth0),{"name":"Hyes_no_unknown","hash":{},"data":data}))
    + "</p>\n    </div>\n";
},"116":function(container,depth0,helpers,partials,data) {
    var stack1;

  return "\n"
    + ((stack1 = (helpers.ifArray || (depth0 && depth0.ifArray) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.judge_or_magistrate_result__1 : depth0),(depth0 != null ? depth0.judge_or_magistrate_result__2 : depth0),(depth0 != null ? depth0.judge_or_magistrate_result__3 : depth0),(depth0 != null ? depth0.judge_or_magistrate_result__4 : depth0),(depth0 != null ? depth0.judge_or_magistrate_resoth : depth0),{"name":"ifArray","hash":{},"fn":container.program(117, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n";
},"117":function(container,depth0,helpers,partials,data) {
    return "    <div class=\"col-sm-6\">\n      <p class=\"kicker\">Judge or Magistrate Result</p>\n    </div>\n    <div class=\"col-sm-6\">\n      <p>"
    + container.escapeExpression((helpers.Hjudge_or_magistrate_result || (depth0 && depth0.Hjudge_or_magistrate_result) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.judge_or_magistrate_result__1 : depth0),(depth0 != null ? depth0.judge_or_magistrate_result__2 : depth0),(depth0 != null ? depth0.judge_or_magistrate_result__3 : depth0),(depth0 != null ? depth0.judge_or_magistrate_result__4 : depth0),(depth0 != null ? depth0.judge_or_magistrate_resoth : depth0),{"name":"Hjudge_or_magistrate_result","hash":{},"data":data}))
    + "</p>\n    </div>\n";
},"119":function(container,depth0,helpers,partials,data) {
    var stack1;

  return "\n  <hr>\n  \n  <div class=\"row\">\n    <div class=\"col-sm-12\">\n      <h4>Detention Locations</h4>\n    </div>\n  </div>\n\n  <div class=\"row\">\n    <div class=\"grid\">\n\n    <div class=\"col-sm-6\">\n      <p class=\"kicker\">Detention locations known</p>\n    </div>\n    <div class=\"col-sm-6\">\n    \n"
    + ((stack1 = helpers.each.call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.where_victim_detained : depth0),{"name":"each","hash":{},"fn":container.program(120, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n    </div>\n\n    </div>\n  </div>\n\n";
},"120":function(container,depth0,helpers,partials,data) {
    var stack1, alias1=depth0 != null ? depth0 : (container.nullContext || {});

  return "\n      <p>"
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.detention_facility_type : depth0),{"name":"if","hash":{},"fn":container.program(121, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.facility_name : depth0),{"name":"if","hash":{},"fn":container.program(123, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.facility_district : depth0),{"name":"if","hash":{},"fn":container.program(125, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.duration_of_detention : depth0),{"name":"if","hash":{},"fn":container.program(127, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n"
    + ((stack1 = (helpers.ifArray || (depth0 && depth0.ifArray) || helpers.helperMissing).call(alias1,(depth0 != null ? depth0.witness_detention___3 : depth0),(depth0 != null ? depth0.witness_detention___4 : depth0),(depth0 != null ? depth0.witness_detention___5 : depth0),(depth0 != null ? depth0.witness_detention___6 : depth0),(depth0 != null ? depth0.witness_detention___7 : depth0),(depth0 != null ? depth0.witness_detention___8 : depth0),(depth0 != null ? depth0.witness_detention___9 : depth0),(depth0 != null ? depth0.witness_detention___10 : depth0),(depth0 != null ? depth0.witness_detention___12 : depth0),(depth0 != null ? depth0.witness_detention___13 : depth0),(depth0 != null ? depth0.witness_detention___14 : depth0),(depth0 != null ? depth0.witness_detention_other : depth0),(depth0 != null ? depth0.witness_detention_status : depth0),{"name":"ifArray","hash":{},"fn":container.program(130, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "      </p>\n\n";
},"121":function(container,depth0,helpers,partials,data) {
    return container.escapeExpression((helpers.Hdetention_facility_type || (depth0 && depth0.Hdetention_facility_type) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.detention_facility_type : depth0),(depth0 != null ? depth0.detention_fac_type_oth : depth0),{"name":"Hdetention_facility_type","hash":{},"data":data}));
},"123":function(container,depth0,helpers,partials,data) {
    return ": "
    + container.escapeExpression((helpers.Hcap || (depth0 && depth0.Hcap) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.facility_name : depth0),{"name":"Hcap","hash":{},"data":data}));
},"125":function(container,depth0,helpers,partials,data) {
    return ", "
    + container.escapeExpression((helpers.Hcap || (depth0 && depth0.Hcap) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.facility_district : depth0),{"name":"Hcap","hash":{},"data":data}));
},"127":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.duration_of_detention : depth0),"Don't know",{"name":"isnot","hash":{},"fn":container.program(128, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"128":function(container,depth0,helpers,partials,data) {
    return ", for "
    + container.escapeExpression((helpers.Hduration_of_detention || (depth0 && depth0.Hduration_of_detention) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.duration_of_detention : depth0),{"name":"Hduration_of_detention","hash":{},"data":data}));
},"130":function(container,depth0,helpers,partials,data) {
    return "        <br>"
    + container.escapeExpression((helpers.Hwitness_detention || (depth0 && depth0.Hwitness_detention) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.witness_detention___3 : depth0),(depth0 != null ? depth0.witness_detention___4 : depth0),(depth0 != null ? depth0.witness_detention___5 : depth0),(depth0 != null ? depth0.witness_detention___6 : depth0),(depth0 != null ? depth0.witness_detention___7 : depth0),(depth0 != null ? depth0.witness_detention___8 : depth0),(depth0 != null ? depth0.witness_detention___9 : depth0),(depth0 != null ? depth0.witness_detention___10 : depth0),(depth0 != null ? depth0.witness_detention___12 : depth0),(depth0 != null ? depth0.witness_detention___13 : depth0),(depth0 != null ? depth0.witness_detention___14 : depth0),(depth0 != null ? depth0.witness_detention_other : depth0),(depth0 != null ? depth0.witness_detention_status : depth0),{"name":"Hwitness_detention","hash":{},"data":data}))
    + "</p>\n";
},"132":function(container,depth0,helpers,partials,data) {
    return "    <h4>Killed"
    + container.escapeExpression((helpers.Hdate || (depth0 && depth0.Hdate) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.victim_death_date : depth0),{"name":"Hdate","hash":{},"data":data}))
    + "</h4>\n";
},"134":function(container,depth0,helpers,partials,data) {
    var stack1, alias1=depth0 != null ? depth0 : (container.nullContext || {}), alias2=helpers.helperMissing;

  return "    <h4>Disappeared"
    + ((stack1 = (helpers.equal || (depth0 && depth0.equal) || alias2).call(alias1,(depth0 != null ? depth0.victim_last_heard_alive : depth0),4,{"name":"equal","hash":{},"fn":container.program(19, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + ((stack1 = (helpers.equal || (depth0 && depth0.equal) || alias2).call(alias1,(depth0 != null ? depth0.victim_last_heard_alive : depth0),1,{"name":"equal","hash":{},"fn":container.program(21, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + ((stack1 = (helpers.equal || (depth0 && depth0.equal) || alias2).call(alias1,(depth0 != null ? depth0.victim_last_heard_alive : depth0),2,{"name":"equal","hash":{},"fn":container.program(23, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + ((stack1 = (helpers.equal || (depth0 && depth0.equal) || alias2).call(alias1,(depth0 != null ? depth0.victim_last_heard_alive : depth0),3,{"name":"equal","hash":{},"fn":container.program(25, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "</h4>\n";
},"136":function(container,depth0,helpers,partials,data) {
    var stack1, alias1=depth0 != null ? depth0 : (container.nullContext || {}), alias2=helpers.helperMissing;

  return "\n  <div class=\"row\">\n    <div class=\"col-sm-12\">\n      <hr>\n      <h5>Disposal of Body</h5>\n    </div>\n  </div>\n\n  <div class=\"row\">\n    <div class=\"grid\">\n\n"
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.so_return_body : depth0),{"name":"if","hash":{},"fn":container.program(137, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n"
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.so_body_disposal : depth0),{"name":"if","hash":{},"fn":container.program(139, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n\n"
    + ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || alias2).call(alias1,(depth0 != null ? depth0.cremation_location_type : depth0),4,{"name":"isnot","hash":{},"fn":container.program(143, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n"
    + ((stack1 = (helpers.ifArray || (depth0 && depth0.ifArray) || alias2).call(alias1,(depth0 != null ? depth0.condition_of_remains___1 : depth0),(depth0 != null ? depth0.condition_of_remains___2 : depth0),(depth0 != null ? depth0.condition_of_remains___3 : depth0),(depth0 != null ? depth0.condition_of_remains___4 : depth0),(depth0 != null ? depth0.condition_of_remains___5 : depth0),(depth0 != null ? depth0.condition_of_remains___6 : depth0),(depth0 != null ? depth0.condition_of_remains___7 : depth0),(depth0 != null ? depth0.other_condition_of_remains : depth0),{"name":"ifArray","hash":{},"fn":container.program(153, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n\n    </div>\n  </div>\n\n";
},"137":function(container,depth0,helpers,partials,data) {
    return "    <div class=\"col-sm-6\">\n      <p class=\"kicker\">Body returned</p>\n    </div>\n    <div class=\"col-sm-6\">\n      <p>"
    + container.escapeExpression((helpers.Hso_return_body || (depth0 && depth0.Hso_return_body) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.so_return_body : depth0),{"name":"Hso_return_body","hash":{},"data":data}))
    + "</p>\n    </div>\n";
},"139":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.so_body_disposal : depth0),5,{"name":"isnot","hash":{},"fn":container.program(140, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"140":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.so_body_disposal : depth0),6,{"name":"isnot","hash":{},"fn":container.program(141, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"141":function(container,depth0,helpers,partials,data) {
    return "    <div class=\"col-sm-6\">\n      <p class=\"kicker\">Body disposal by security forces</p>\n    </div>\n    <div class=\"col-sm-6\">\n      <p>"
    + container.escapeExpression((helpers.Hso_body_disposal || (depth0 && depth0.Hso_body_disposal) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.so_body_disposal : depth0),{"name":"Hso_body_disposal","hash":{},"data":data}))
    + "</p>\n    </div>\n";
},"143":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = helpers["if"].call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.cremation_location_type : depth0),{"name":"if","hash":{},"fn":container.program(144, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"144":function(container,depth0,helpers,partials,data) {
    var stack1, alias1=depth0 != null ? depth0 : (container.nullContext || {}), alias2=helpers.helperMissing;

  return "    <div class=\"col-sm-6\">\n      <p class=\"kicker\">Cremation location</p>    \n    </div>\n    <div class=\"col-sm-6\">\n      <p>\n      "
    + ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || alias2).call(alias1,(depth0 != null ? depth0.cremation_location_type : depth0),5,{"name":"isnot","hash":{},"fn":container.program(145, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + ((stack1 = (helpers.equal || (depth0 && depth0.equal) || alias2).call(alias1,(depth0 != null ? depth0.cremation_location_type : depth0),5,{"name":"equal","hash":{},"fn":container.program(147, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.cremation_location_name : depth0),{"name":"if","hash":{},"fn":container.program(150, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n      </p>\n    </div>\n";
},"145":function(container,depth0,helpers,partials,data) {
    return container.escapeExpression((helpers.Hcremation_location_type || (depth0 && depth0.Hcremation_location_type) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.cremation_location_type : depth0),{"name":"Hcremation_location_type","hash":{},"data":data}));
},"147":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = helpers["if"].call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.cremation_loctype_other : depth0),{"name":"if","hash":{},"fn":container.program(148, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"148":function(container,depth0,helpers,partials,data) {
    var helper;

  return container.escapeExpression(((helper = (helper = helpers.cremation_loctype_other || (depth0 != null ? depth0.cremation_loctype_other : depth0)) != null ? helper : helpers.helperMissing),(typeof helper === "function" ? helper.call(depth0 != null ? depth0 : (container.nullContext || {}),{"name":"cremation_loctype_other","hash":{},"data":data}) : helper)));
},"150":function(container,depth0,helpers,partials,data) {
    var stack1, alias1=depth0 != null ? depth0 : (container.nullContext || {}), alias2=helpers.helperMissing;

  return ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || alias2).call(alias1,(depth0 != null ? depth0.cremation_location_type : depth0),5,{"name":"isnot","hash":{},"fn":container.program(151, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + container.escapeExpression((helpers.Hcap || (depth0 && depth0.Hcap) || alias2).call(alias1,(depth0 != null ? depth0.cremation_location_name : depth0),{"name":"Hcap","hash":{},"data":data}));
},"151":function(container,depth0,helpers,partials,data) {
    return ", ";
},"153":function(container,depth0,helpers,partials,data) {
    return "\n    <div class=\"col-sm-6\">\n      <p class=\"kicker\">Condition of remains</p>      \n    </div>\n    <div class=\"col-sm-6\">\n      <p>"
    + container.escapeExpression((helpers.Hcondition_of_remains || (depth0 && depth0.Hcondition_of_remains) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.condition_of_remains___1 : depth0),(depth0 != null ? depth0.condition_of_remains___2 : depth0),(depth0 != null ? depth0.condition_of_remains___3 : depth0),(depth0 != null ? depth0.condition_of_remains___4 : depth0),(depth0 != null ? depth0.condition_of_remains___5 : depth0),(depth0 != null ? depth0.condition_of_remains___6 : depth0),(depth0 != null ? depth0.condition_of_remains___7 : depth0),(depth0 != null ? depth0.other_condition_of_remains : depth0),{"name":"Hcondition_of_remains","hash":{},"data":data}))
    + "</p>\n    </div>\n\n";
},"155":function(container,depth0,helpers,partials,data) {
    return "\n  <hr>\n  <div class=\"row\">\n    <div class=\"col-sm-12\">\n      <h4>Security Forces Implicated</h4>\n    </div>\n  </div>  \n\n";
},"157":function(container,depth0,helpers,partials,data) {
    return "    <div class=\"col-sm-6\">\n      <p class=\"kicker\">Forces involved in abduction/arrest</p>\n    </div>\n    <div class=\"col-sm-6\">\n      <p>"
    + container.escapeExpression((helpers.Harrest_security_type || (depth0 && depth0.Harrest_security_type) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.arrest_security_type___1 : depth0),(depth0 != null ? depth0.arrest_security_type___2 : depth0),(depth0 != null ? depth0.arrest_security_type___3 : depth0),(depth0 != null ? depth0.arrest_security_type___4 : depth0),(depth0 != null ? depth0.arrest_security_type___5 : depth0),(depth0 != null ? depth0.arrest_security_type___6 : depth0),(depth0 != null ? depth0.arrest_security_type___7 : depth0),(depth0 != null ? depth0.arrest_security_type___8 : depth0),(depth0 != null ? depth0.arrest_security_type_oth : depth0),{"name":"Harrest_security_type","hash":{},"data":data}))
    + "</p>\n    </div>\n";
},"159":function(container,depth0,helpers,partials,data) {
    var stack1;

  return "\n  <!-- arresting -->\n\n    <div class=\"col-sm-6\">\n      <p class=\"kicker\">Security officials involved in abduction</p>\n    </div>\n    <div class=\"col-sm-6\">\n\n"
    + ((stack1 = helpers.each.call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.security_arrest : depth0),{"name":"each","hash":{},"fn":container.program(160, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n    </div>\n\n\n";
},"160":function(container,depth0,helpers,partials,data) {
    var stack1, alias1=depth0 != null ? depth0 : (container.nullContext || {}), alias2=helpers.helperMissing, alias3=container.escapeExpression;

  return "\n      <p>"
    + alias3((helpers.Hcap || (depth0 && depth0.Hcap) || alias2).call(alias1,(depth0 != null ? depth0.arrest_so_first_name : depth0),{"name":"Hcap","hash":{},"data":data}))
    + " "
    + alias3((helpers.Hcap || (depth0 && depth0.Hcap) || alias2).call(alias1,(depth0 != null ? depth0.arrest_so_last_name : depth0),{"name":"Hcap","hash":{},"data":data}))
    + "<!-- rank -->"
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.arrest_so_rank : depth0),{"name":"if","hash":{},"fn":container.program(161, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "<!-- affiliaton -->"
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.arrest_so_affiliation : depth0),{"name":"if","hash":{},"fn":container.program(168, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "<!-- arrest_so_affiliation_oth -->"
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.arrest_so_affiliation_oth : depth0),{"name":"if","hash":{},"fn":container.program(172, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.arrest_so_affiliation_loc : depth0),{"name":"if","hash":{},"fn":container.program(174, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.arrest_security_locality : depth0),{"name":"if","hash":{},"fn":container.program(176, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "</p>\n\n";
},"161":function(container,depth0,helpers,partials,data) {
    var stack1, alias1=depth0 != null ? depth0 : (container.nullContext || {}), alias2=helpers.helperMissing;

  return ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || alias2).call(alias1,(depth0 != null ? depth0.arrest_so_rank : depth0),13,{"name":"isnot","hash":{},"fn":container.program(162, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + ((stack1 = (helpers.equal || (depth0 && depth0.equal) || alias2).call(alias1,(depth0 != null ? depth0.arrest_so_rank : depth0),13,{"name":"equal","hash":{},"fn":container.program(165, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"162":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.arrest_so_rank : depth0),14,{"name":"isnot","hash":{},"fn":container.program(163, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"163":function(container,depth0,helpers,partials,data) {
    return ", \n"
    + container.escapeExpression((helpers.Harrest_so_rank || (depth0 && depth0.Harrest_so_rank) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.arrest_so_rank : depth0),{"name":"Harrest_so_rank","hash":{},"data":data}));
},"165":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = helpers["if"].call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.arrest_so_rank_other : depth0),{"name":"if","hash":{},"fn":container.program(166, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"166":function(container,depth0,helpers,partials,data) {
    return ", \n"
    + container.escapeExpression(container.lambda((depth0 != null ? depth0.arrest_so_rank_other : depth0), depth0));
},"168":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.arrest_so_affiliation : depth0),8,{"name":"isnot","hash":{},"fn":container.program(169, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"169":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.arrest_so_affiliation : depth0),7,{"name":"isnot","hash":{},"fn":container.program(170, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"170":function(container,depth0,helpers,partials,data) {
    return ", \n"
    + container.escapeExpression((helpers.Haffiliation || (depth0 && depth0.Haffiliation) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.arrest_so_affiliation : depth0),{"name":"Haffiliation","hash":{},"data":data}));
},"172":function(container,depth0,helpers,partials,data) {
    return ", \n"
    + container.escapeExpression(container.lambda((depth0 != null ? depth0.arrest_so_affiliation_oth : depth0), depth0));
},"174":function(container,depth0,helpers,partials,data) {
    return ", "
    + container.escapeExpression(container.lambda((depth0 != null ? depth0.arrest_so_affiliation_loc : depth0), depth0));
},"176":function(container,depth0,helpers,partials,data) {
    return ", "
    + container.escapeExpression(container.lambda((depth0 != null ? depth0.arrest_security_locality : depth0), depth0));
},"178":function(container,depth0,helpers,partials,data) {
    var stack1, alias1=depth0 != null ? depth0 : (container.nullContext || {});

  return "\n    <div class=\"col-sm-6\">\n      <p class=\"kicker\">Forces involved in killing</p>\n    </div>\n    <div class=\"col-sm-6\">\n      <p>"
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.killing_securityforces_lcl : depth0),{"name":"if","hash":{},"fn":container.program(179, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + " "
    + container.escapeExpression((helpers.Harrest_security_type || (depth0 && depth0.Harrest_security_type) || helpers.helperMissing).call(alias1,(depth0 != null ? depth0.killing_securityforcestype__1 : depth0),(depth0 != null ? depth0.killing_securityforcestype__2 : depth0),(depth0 != null ? depth0.killing_securityforcestype__3 : depth0),(depth0 != null ? depth0.killing_securityforcestype__4 : depth0),(depth0 != null ? depth0.killing_securityforcestype__5 : depth0),(depth0 != null ? depth0.killing_securityforcestype__6 : depth0),(depth0 != null ? depth0.killing_securityforcestype__6 : depth0),(depth0 != null ? depth0.killing_securityforcestype__7 : depth0),(depth0 != null ? depth0.killing_securityforcestype__8 : depth0),(depth0 != null ? depth0.killing_securityforces_oth : depth0),{"name":"Harrest_security_type","hash":{},"data":data}))
    + "</p>\n    </div>\n\n";
},"179":function(container,depth0,helpers,partials,data) {
    return container.escapeExpression((helpers.Hcap || (depth0 && depth0.Hcap) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.killing_securityforces_lcl : depth0),{"name":"Hcap","hash":{},"data":data}));
},"181":function(container,depth0,helpers,partials,data) {
    var stack1;

  return "\n    <div class=\"col-sm-6\">\n      <p class=\"kicker\">Security official involved in killing</p>\n    </div>\n    <div class=\"col-sm-6\">\n\n"
    + ((stack1 = helpers.each.call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.security_killed : depth0),{"name":"each","hash":{},"fn":container.program(182, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n    </div>\n\n";
},"182":function(container,depth0,helpers,partials,data) {
    var stack1, alias1=depth0 != null ? depth0 : (container.nullContext || {}), alias2=helpers.helperMissing, alias3=container.escapeExpression;

  return "\n      <p>"
    + alias3((helpers.Hcap || (depth0 && depth0.Hcap) || alias2).call(alias1,(depth0 != null ? depth0.killing_so_first_name : depth0),{"name":"Hcap","hash":{},"data":data}))
    + " "
    + alias3((helpers.Hcap || (depth0 && depth0.Hcap) || alias2).call(alias1,(depth0 != null ? depth0.killing_so_last_name : depth0),{"name":"Hcap","hash":{},"data":data}))
    + "<!-- rank -->"
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.killing_so_rank : depth0),{"name":"if","hash":{},"fn":container.program(183, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "<!-- affiliation -->"
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.killing_so_affiliation : depth0),{"name":"if","hash":{},"fn":container.program(190, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "<!-- killing_so_affiliation_oth -->"
    + ((stack1 = (helpers.equal || (depth0 && depth0.equal) || alias2).call(alias1,(depth0 != null ? depth0.killing_so_affiliation : depth0),8,{"name":"equal","hash":{},"fn":container.program(194, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.killing_so_affiliation_loc : depth0),{"name":"if","hash":{},"fn":container.program(197, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + " </p>\n\n";
},"183":function(container,depth0,helpers,partials,data) {
    var stack1, alias1=depth0 != null ? depth0 : (container.nullContext || {}), alias2=helpers.helperMissing;

  return ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || alias2).call(alias1,(depth0 != null ? depth0.killing_so_rank : depth0),13,{"name":"isnot","hash":{},"fn":container.program(184, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + ((stack1 = (helpers.equal || (depth0 && depth0.equal) || alias2).call(alias1,(depth0 != null ? depth0.killing_so_rank : depth0),13,{"name":"equal","hash":{},"fn":container.program(187, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"184":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.killing_so_rank : depth0),14,{"name":"isnot","hash":{},"fn":container.program(185, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"185":function(container,depth0,helpers,partials,data) {
    return ", "
    + container.escapeExpression((helpers.Harrest_so_rank || (depth0 && depth0.Harrest_so_rank) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.killing_so_rank : depth0),{"name":"Harrest_so_rank","hash":{},"data":data}));
},"187":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = helpers["if"].call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.killing_so_rank_other : depth0),{"name":"if","hash":{},"fn":container.program(188, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"188":function(container,depth0,helpers,partials,data) {
    return ", "
    + container.escapeExpression(container.lambda((depth0 != null ? depth0.killing_so_rank_other : depth0), depth0));
},"190":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.killing_so_affiliation : depth0),8,{"name":"isnot","hash":{},"fn":container.program(191, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"191":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.killing_so_affiliation : depth0),7,{"name":"isnot","hash":{},"fn":container.program(192, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"192":function(container,depth0,helpers,partials,data) {
    return ", "
    + container.escapeExpression((helpers.Haffiliation || (depth0 && depth0.Haffiliation) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.killing_so_affiliation : depth0),{"name":"Haffiliation","hash":{},"data":data}));
},"194":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = helpers["if"].call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.killing_so_affiliation_oth : depth0),{"name":"if","hash":{},"fn":container.program(195, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"195":function(container,depth0,helpers,partials,data) {
    return ", "
    + container.escapeExpression(container.lambda((depth0 != null ? depth0.killing_so_affiliation_oth : depth0), depth0));
},"197":function(container,depth0,helpers,partials,data) {
    return ", "
    + container.escapeExpression(container.lambda((depth0 != null ? depth0.killing_so_affiliation_loc : depth0), depth0));
},"199":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.security_official_response__14 : depth0),1,{"name":"isnot","hash":{},"fn":container.program(200, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"200":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.court_or_commission : depth0),9,{"name":"isnot","hash":{},"fn":container.program(201, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"201":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.govnt_response_desired___11 : depth0),1,{"name":"isnot","hash":{},"fn":container.program(202, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"202":function(container,depth0,helpers,partials,data) {
    return "\n  <hr>  \n\n  <div class=\"row\">\n    <div class=\"col-sm-12\">\n      <h4>Advocacy & Impact</h4>\n    </div>\n  </div>\n\n";
},"204":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = helpers["if"].call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.security_officials_apprchd : depth0),{"name":"if","hash":{},"fn":container.program(205, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"205":function(container,depth0,helpers,partials,data) {
    var stack1, alias1=depth0 != null ? depth0 : (container.nullContext || {}), alias2=helpers.helperMissing;

  return "    <div class=\"col-sm-6\">\n      <p class=\"kicker\">Security officlals approached</p>\n    </div>\n    <div class=\"col-sm-6\">\n      <p>"
    + container.escapeExpression((helpers.Hyes_no || (depth0 && depth0.Hyes_no) || alias2).call(alias1,(depth0 != null ? depth0.security_officials_apprchd : depth0),{"name":"Hyes_no","hash":{},"data":data}))
    + ((stack1 = (helpers.ifArray || (depth0 && depth0.ifArray) || alias2).call(alias1,(depth0 != null ? depth0.so_approached_type__1 : depth0),(depth0 != null ? depth0.so_approached_type__2 : depth0),(depth0 != null ? depth0.so_approached_type__3 : depth0),(depth0 != null ? depth0.so_approached_type__4 : depth0),(depth0 != null ? depth0.so_approached_type__5 : depth0),(depth0 != null ? depth0.so_approached_type__6 : depth0),(depth0 != null ? depth0.so_approached_type__7 : depth0),(depth0 != null ? depth0.so_approached_other : depth0),{"name":"ifArray","hash":{},"fn":container.program(206, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.so_approached_loc : depth0),{"name":"if","hash":{},"fn":container.program(208, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "</p>\n    </div>\n";
},"206":function(container,depth0,helpers,partials,data) {
    return container.escapeExpression((helpers.Hso_approached_type || (depth0 && depth0.Hso_approached_type) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.so_approached_type__1 : depth0),(depth0 != null ? depth0.so_approached_type__2 : depth0),(depth0 != null ? depth0.so_approached_type__3 : depth0),(depth0 != null ? depth0.so_approached_type__4 : depth0),(depth0 != null ? depth0.so_approached_type__5 : depth0),(depth0 != null ? depth0.so_approached_type__6 : depth0),(depth0 != null ? depth0.so_approached_type__7 : depth0),(depth0 != null ? depth0.so_approached_other : depth0),{"name":"Hso_approached_type","hash":{},"data":data}));
},"208":function(container,depth0,helpers,partials,data) {
    return ", from "
    + container.escapeExpression((helpers.Hadd_spaces || (depth0 && depth0.Hadd_spaces) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.so_approached_loc : depth0),{"name":"Hadd_spaces","hash":{},"data":data}));
},"210":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = (helpers.ifArray || (depth0 && depth0.ifArray) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.security_official_response__0 : depth0),(depth0 != null ? depth0.security_official_response__1 : depth0),(depth0 != null ? depth0.security_official_response__2 : depth0),(depth0 != null ? depth0.security_official_response__3 : depth0),(depth0 != null ? depth0.security_official_response__4 : depth0),(depth0 != null ? depth0.security_official_response__5 : depth0),(depth0 != null ? depth0.security_official_response__6 : depth0),(depth0 != null ? depth0.security_official_response__7 : depth0),(depth0 != null ? depth0.security_official_response__8 : depth0),(depth0 != null ? depth0.security_official_response__9 : depth0),(depth0 != null ? depth0.security_official_response__10 : depth0),(depth0 != null ? depth0.security_official_response__11 : depth0),(depth0 != null ? depth0.security_official_response__12 : depth0),(depth0 != null ? depth0.security_official_response__13 : depth0),(depth0 != null ? depth0.security_official_response__14 : depth0),(depth0 != null ? depth0.other_so_response : depth0),{"name":"ifArray","hash":{},"fn":container.program(211, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"211":function(container,depth0,helpers,partials,data) {
    return "    <div class=\"col-sm-6\">\n      <p class=\"kicker\">Security official response</p>\n    </div>\n    <div class=\"col-sm-6\">\n      <p>"
    + container.escapeExpression((helpers.Hsecurity_official_response || (depth0 && depth0.Hsecurity_official_response) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.security_official_response__0 : depth0),(depth0 != null ? depth0.security_official_response__1 : depth0),(depth0 != null ? depth0.security_official_response__2 : depth0),(depth0 != null ? depth0.security_official_response__3 : depth0),(depth0 != null ? depth0.security_official_response__4 : depth0),(depth0 != null ? depth0.security_official_response__5 : depth0),(depth0 != null ? depth0.security_official_response__6 : depth0),(depth0 != null ? depth0.security_official_response__7 : depth0),(depth0 != null ? depth0.security_official_response__8 : depth0),(depth0 != null ? depth0.security_official_response__9 : depth0),(depth0 != null ? depth0.security_official_response__10 : depth0),(depth0 != null ? depth0.security_official_response__11 : depth0),(depth0 != null ? depth0.security_official_response__12 : depth0),(depth0 != null ? depth0.security_official_response__13 : depth0),(depth0 != null ? depth0.security_official_response__14 : depth0),(depth0 != null ? depth0.other_so_response : depth0),{"name":"Hsecurity_official_response","hash":{},"data":data}))
    + "</p>\n    </div>\n";
},"213":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.court_or_commission : depth0),9,{"name":"isnot","hash":{},"fn":container.program(214, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"214":function(container,depth0,helpers,partials,data) {
    var stack1, alias1=depth0 != null ? depth0 : (container.nullContext || {}), alias2=helpers.helperMissing;

  return "    <div class=\"col-sm-6\">\n      <p class=\"kicker\">Legal remedies pursued</p>\n    </div>\n    <div class=\"col-sm-6\">\n      <p>"
    + container.escapeExpression((helpers.Hyes_no || (depth0 && depth0.Hyes_no) || alias2).call(alias1,(depth0 != null ? depth0.court_or_commission : depth0),{"name":"Hyes_no","hash":{},"data":data}))
    + ((stack1 = (helpers.ifArray || (depth0 && depth0.ifArray) || alias2).call(alias1,(depth0 != null ? depth0.no_action_pursued_reason___1 : depth0),(depth0 != null ? depth0.no_action_pursued_reason___2 : depth0),(depth0 != null ? depth0.no_action_pursued_reason___3 : depth0),(depth0 != null ? depth0.no_action_pursued_reason___4 : depth0),(depth0 != null ? depth0.other_no_action_reason : depth0),{"name":"ifArray","hash":{},"fn":container.program(215, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "</p>\n    </div>\n";
},"215":function(container,depth0,helpers,partials,data) {
    return ", "
    + container.escapeExpression((helpers.Hno_action_pursued_reason || (depth0 && depth0.Hno_action_pursued_reason) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.no_action_pursued_reason___1 : depth0),(depth0 != null ? depth0.no_action_pursued_reason___2 : depth0),(depth0 != null ? depth0.no_action_pursued_reason___3 : depth0),(depth0 != null ? depth0.no_action_pursued_reason___4 : depth0),(depth0 != null ? depth0.other_no_action_reason : depth0),{"name":"Hno_action_pursued_reason","hash":{},"data":data}));
},"217":function(container,depth0,helpers,partials,data) {
    return "    <div class=\"col-sm-6\">\n      <p class=\"kicker\">Impact on family</p>      \n    </div>\n    <div class=\"col-sm-6\">\n      <p>"
    + container.escapeExpression((helpers.Hfamily_effects || (depth0 && depth0.Hfamily_effects) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.family_effects___1 : depth0),(depth0 != null ? depth0.family_effects___2 : depth0),(depth0 != null ? depth0.family_effects___3 : depth0),(depth0 != null ? depth0.family_effects___4 : depth0),(depth0 != null ? depth0.family_effects___5 : depth0),(depth0 != null ? depth0.family_effects___6 : depth0),(depth0 != null ? depth0.family_effects___7 : depth0),(depth0 != null ? depth0.family_effects___8 : depth0),(depth0 != null ? depth0.family_effects___9 : depth0),(depth0 != null ? depth0.family_effects___12 : depth0),(depth0 != null ? depth0.other_family_effects : depth0),{"name":"Hfamily_effects","hash":{},"data":data}))
    + "</p>\n    </div>\n";
},"219":function(container,depth0,helpers,partials,data) {
    return "    <div class=\"col-sm-6\">\n      <p class=\"kicker\">Response desired by Government</p>\n    </div>\n    <div class=\"col-sm-6\">\n      <p>"
    + container.escapeExpression((helpers.Hgovnt_response_desired || (depth0 && depth0.Hgovnt_response_desired) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.govnt_response_desired___1 : depth0),(depth0 != null ? depth0.govnt_response_desired___2 : depth0),(depth0 != null ? depth0.govnt_response_desired___3 : depth0),(depth0 != null ? depth0.govnt_response_desired___4 : depth0),(depth0 != null ? depth0.govnt_response_desired___5 : depth0),(depth0 != null ? depth0.govnt_response_desired___6 : depth0),(depth0 != null ? depth0.govnt_response_desired___7 : depth0),(depth0 != null ? depth0.govnt_response_desired___8 : depth0),(depth0 != null ? depth0.govnt_response_desired___9 : depth0),(depth0 != null ? depth0.govnt_response_desired___10 : depth0),(depth0 != null ? depth0.govnt_response_desired___11 : depth0),(depth0 != null ? depth0.other_govnt_response_desired : depth0),{"name":"Hgovnt_response_desired","hash":{},"data":data}))
    + "</p>\n    </div>\n  </div>\n";
},"221":function(container,depth0,helpers,partials,data) {
    var helper;

  return "  <div class=\"row\">\n    <div class=\"col-sm-6\">\n      <p class=\"kicker\">Unlawful killings/disappearances in family</p>\n    </div>\n    <div class=\"col-sm-6\">\n      <p>"
    + container.escapeExpression(((helper = (helper = helpers.number_of_victims || (depth0 != null ? depth0.number_of_victims : depth0)) != null ? helper : helpers.helperMissing),(typeof helper === "function" ? helper.call(depth0 != null ? depth0 : (container.nullContext || {}),{"name":"number_of_victims","hash":{},"data":data}) : helper)))
    + "</p>\n    </div>\n  </div>\n";
},"223":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.genuine_encounters : depth0),9,{"name":"isnot","hash":{},"fn":container.program(224, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"224":function(container,depth0,helpers,partials,data) {
    return "  <div class=\"row\">\n    <div class=\"col-sm-6\">\n      <p class=\"kicker\">Genuine encounters in family</p>\n    </div>\n    <div class=\"col-sm-6\">\n      <p>"
    + container.escapeExpression((helpers.Hyes_no || (depth0 && depth0.Hyes_no) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.genuine_encounters : depth0),{"name":"Hyes_no","hash":{},"data":data}))
    + "</p>\n    </div>\n  </div>\n";
},"226":function(container,depth0,helpers,partials,data) {
    return "  <div class=\"row\">\n    <div class=\"col-sm-6\">\n      <p class=\"kicker\">Co-victims of abduction/arrest</p>\n    </div>\n    <div class=\"col-sm-6\">\n      <p>"
    + container.escapeExpression((helpers.Hothers_arrested || (depth0 && depth0.Hothers_arrested) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.others_arrested : depth0),{"name":"Hothers_arrested","hash":{},"data":data}))
    + "</p>\n    </div>\n  </div>\n";
},"228":function(container,depth0,helpers,partials,data) {
    var stack1;

  return ((stack1 = (helpers.ifArray || (depth0 && depth0.ifArray) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.others_killed___0 : depth0),(depth0 != null ? depth0.others_killed___1 : depth0),(depth0 != null ? depth0.others_killed___2 : depth0),(depth0 != null ? depth0.others_killed___3 : depth0),(depth0 != null ? depth0.others_killed___9 : depth0),{"name":"ifArray","hash":{},"fn":container.program(229, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "");
},"229":function(container,depth0,helpers,partials,data) {
    return "  <div class=\"row\">\n    <div class=\"col-sm-6\">\n      <p class=\"kicker\">Co-victims of killing</p>\n    </div>\n    <div class=\"col-sm-6\">\n      <p>"
    + container.escapeExpression((helpers.Hothers_killed || (depth0 && depth0.Hothers_killed) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.others_killed___0 : depth0),(depth0 != null ? depth0.others_killed___1 : depth0),(depth0 != null ? depth0.others_killed___2 : depth0),(depth0 != null ? depth0.others_killed___3 : depth0),(depth0 != null ? depth0.others_killed___9 : depth0),{"name":"Hothers_killed","hash":{},"data":data}))
    + "</p>\n    </div>\n  </div>\n";
},"231":function(container,depth0,helpers,partials,data) {
    var stack1;

  return "\n  <hr>  \n\n  <div class=\"row\">\n    <div class=\"col-sm-12\">\n      <h4></h4>\n    </div>\n  </div>\n\n  <div class=\"row\">\n    <div class=\"col-sm-12 documents\">\n      "
    + ((stack1 = (helpers.Hphoto || (depth0 && depth0.Hphoto) || helpers.helperMissing).call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.photo_doc_fn : depth0),{"name":"Hphoto","hash":{},"data":data})) != null ? stack1 : "")
    + "\n    </div>\n  </div>\n\n\n";
},"compiler":[7,">= 4.0.0"],"main":function(container,depth0,helpers,partials,data) {
    var stack1, helper, alias1=depth0 != null ? depth0 : (container.nullContext || {}), alias2=helpers.helperMissing, alias3=container.escapeExpression;

  return "  <div class=\"row\">\n \n"
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.photo_vic_fn : depth0),{"name":"if","hash":{},"fn":container.program(1, data, 0),"inverse":container.program(3, data, 0),"data":data})) != null ? stack1 : "")
    + "\n\n      <h1>"
    + alias3(((helper = (helper = helpers.victim_name || (depth0 != null ? depth0.victim_name : depth0)) != null ? helper : alias2),(typeof helper === "function" ? helper.call(alias1,{"name":"victim_name","hash":{},"data":data}) : helper)))
    + "</h1>\n\n      <p>\n      "
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.victim_sex : depth0),{"name":"if","hash":{},"fn":container.program(5, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.victim_age : depth0),{"name":"if","hash":{},"fn":container.program(7, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n      </p>\n\n"
    + ((stack1 = (helpers.equal || (depth0 && depth0.equal) || alias2).call(alias1,(depth0 != null ? depth0.victim_disappeared_killed : depth0),2,{"name":"equal","hash":{},"fn":container.program(16, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n"
    + ((stack1 = (helpers.equal || (depth0 && depth0.equal) || alias2).call(alias1,(depth0 != null ? depth0.victim_disappeared_killed : depth0),1,{"name":"equal","hash":{},"fn":container.program(18, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n      <hr>  \n    \n      <h4>Profile</h4>\n\n"
    + ((stack1 = (helpers.equal || (depth0 && depth0.equal) || alias2).call(alias1,(depth0 != null ? depth0.victim_address_int_loc : depth0),1,{"name":"equal","hash":{},"fn":container.program(27, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n"
    + ((stack1 = (helpers.equal || (depth0 && depth0.equal) || alias2).call(alias1,(depth0 != null ? depth0.victim_address_int_loc : depth0),0,{"name":"equal","hash":{},"fn":container.program(30, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n\n  \n"
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.victim_education : depth0),{"name":"if","hash":{},"fn":container.program(33, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n\n"
    + ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || alias2).call(alias1,(depth0 != null ? depth0.victim_employment___10 : depth0),1,{"name":"isnot","hash":{},"fn":container.program(36, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n"
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.victim_employment_other : depth0),{"name":"if","hash":{},"fn":container.program(40, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n"
    + ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || alias2).call(alias1,(depth0 != null ? depth0.victim_marital_status : depth0),9,{"name":"isnot","hash":{},"fn":container.program(42, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "    \n    \n    \n"
    + ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || alias2).call(alias1,(depth0 != null ? depth0.victim_religion : depth0),6,{"name":"isnot","hash":{},"fn":container.program(46, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n"
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.victim_religion_other : depth0),{"name":"if","hash":{},"fn":container.program(52, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n\n"
    + ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || alias2).call(alias1,(depth0 != null ? depth0.victim_caste : depth0),8,{"name":"isnot","hash":{},"fn":container.program(54, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n\n"
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.victim_dob : depth0),{"name":"if","hash":{},"fn":container.program(57, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n    </div>\n"
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.photo_vic_fn : depth0),{"name":"if","hash":{},"fn":container.program(59, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "  </div>\n  \n\n\n\n\n  <hr>\n\n\n\n  <div class=\"row\">\n    <div class=\"col-sm-12\">\n      <h4>The Militancy & Prior Abuse</h4>\n    </div>\n  </div>\n  \n\n  <div class=\"row\">\n\n\n    <div class=\"col-sm-6\">\n      <p class=\"kicker\">Militant</p>\n    </div>\n    <div class=\"col-sm-6\">\n      <p>"
    + alias3((helpers.Hyes_no_unknown || (depth0 && depth0.Hyes_no_unknown) || alias2).call(alias1,(depth0 != null ? depth0.victim_militant_status : depth0),{"name":"Hyes_no_unknown","hash":{},"data":data}))
    + "</p>\n    </div>\n\n\n\n\n"
    + ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || alias2).call(alias1,(depth0 != null ? depth0.victim_militant_reason___7 : depth0),1,{"name":"isnot","hash":{},"fn":container.program(61, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n"
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.victim_militant_reason_oth : depth0),{"name":"if","hash":{},"fn":container.program(66, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n  \n\n\n"
    + ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || alias2).call(alias1,(depth0 != null ? depth0.victim_militant_support : depth0),9,{"name":"isnot","hash":{},"fn":container.program(68, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n"
    + ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || alias2).call(alias1,(depth0 != null ? depth0.victim_prior_detention_st : depth0),9,{"name":"isnot","hash":{},"fn":container.program(73, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n"
    + ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || alias2).call(alias1,(depth0 != null ? depth0.victim_prior_detention_trt : depth0),3,{"name":"isnot","hash":{},"fn":container.program(77, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n  </div>\n  \n  \n\n\n  <hr>\n\n\n  <div class=\"row\">\n    <div class=\"col-sm-12\">\n      <h4>Abduction, Detention, Unlawful Killing, or Disappearance</h4>\n    </div>\n  </div>\n\n  <div class=\"row\">\n    <div class=\"grid\">\n  \n"
    + ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || alias2).call(alias1,(depth0 != null ? depth0.target_reason___8 : depth0),1,{"name":"isnot","hash":{},"fn":container.program(81, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n"
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.target_reason_other : depth0),{"name":"if","hash":{},"fn":container.program(85, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n\n"
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.victim_arrest_status : depth0),{"name":"if","hash":{},"fn":container.program(87, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n"
    + ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || alias2).call(alias1,(depth0 != null ? depth0.victim_arrest_location : depth0),1,{"name":"isnot","hash":{},"fn":container.program(90, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n\n"
    + ((stack1 = (helpers.ifArray || (depth0 && depth0.ifArray) || alias2).call(alias1,(depth0 != null ? depth0.witness_arrest___0 : depth0),(depth0 != null ? depth0.witness_arrest___1 : depth0),(depth0 != null ? depth0.witness_arrest___2 : depth0),(depth0 != null ? depth0.witness_arrest___3 : depth0),(depth0 != null ? depth0.witness_arrest___4 : depth0),(depth0 != null ? depth0.witness_arrest___5 : depth0),(depth0 != null ? depth0.witness_arrest___6 : depth0),(depth0 != null ? depth0.witness_arrest___7 : depth0),(depth0 != null ? depth0.witness_arrest___8 : depth0),(depth0 != null ? depth0.witness_arrest___9 : depth0),(depth0 != null ? depth0.witness_arrest___10 : depth0),(depth0 != null ? depth0.witness_arrest___12 : depth0),(depth0 != null ? depth0.witness_arrest_oth : depth0),{"name":"ifArray","hash":{},"fn":container.program(101, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n\n\n\n"
    + ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || alias2).call(alias1,(depth0 != null ? depth0.so_inform_witnesses : depth0),9,{"name":"isnot","hash":{},"fn":container.program(103, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n\n\n"
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.security_forces_uniformed : depth0),{"name":"if","hash":{},"fn":container.program(107, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n\n"
    + ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || alias2).call(alias1,(depth0 != null ? depth0.demands___9 : depth0),1,{"name":"isnot","hash":{},"fn":container.program(110, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n\n"
    + ((stack1 = (helpers.equalor || (depth0 && depth0.equalor) || alias2).call(alias1,(depth0 != null ? depth0.victim_arrest_status : depth0),2,(depth0 != null ? depth0.victim_arrest_status : depth0),1,{"name":"equalor","hash":{},"fn":container.program(114, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n"
    + ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || alias2).call(alias1,(depth0 != null ? depth0.judge_or_magistrate_result__3 : depth0),1,{"name":"isnot","hash":{},"fn":container.program(116, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n\n    </div>\n  </div>\n\n\n"
    + ((stack1 = helpers["if"].call(alias1,((stack1 = ((stack1 = (depth0 != null ? depth0.where_victim_detained : depth0)) != null ? stack1["0"] : stack1)) != null ? stack1.detention_facility_type : stack1),{"name":"if","hash":{},"fn":container.program(119, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n\n\n\n\n  <hr>\n  \n  <div class=\"row\">\n    <div class=\"col-sm-12\">\n\n"
    + ((stack1 = (helpers.equal || (depth0 && depth0.equal) || alias2).call(alias1,(depth0 != null ? depth0.victim_disappeared_killed : depth0),2,{"name":"equal","hash":{},"fn":container.program(132, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n"
    + ((stack1 = (helpers.equal || (depth0 && depth0.equal) || alias2).call(alias1,(depth0 != null ? depth0.victim_disappeared_killed : depth0),1,{"name":"equal","hash":{},"fn":container.program(134, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n      <p class=\"kicker\"><em><strong>Additional data forthcoming</strong></em></p>\n\n    </div>\n  </div>\n\n\n\n\n\n"
    + ((stack1 = (helpers.equal || (depth0 && depth0.equal) || alias2).call(alias1,(depth0 != null ? depth0.victim_disappeared_killed : depth0),2,{"name":"equal","hash":{},"fn":container.program(136, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "<!-- #equal victim_disappeared_killed 2 -->\n\n\n\n\n"
    + ((stack1 = (helpers.ifArray || (depth0 && depth0.ifArray) || alias2).call(alias1,(depth0 != null ? depth0.arrest_security_type___1 : depth0),(depth0 != null ? depth0.arrest_security_type___2 : depth0),(depth0 != null ? depth0.arrest_security_type___3 : depth0),(depth0 != null ? depth0.arrest_security_type___4 : depth0),(depth0 != null ? depth0.arrest_security_type___5 : depth0),(depth0 != null ? depth0.arrest_security_type___6 : depth0),(depth0 != null ? depth0.arrest_security_type___7 : depth0),(depth0 != null ? depth0.security_killed : depth0),{"name":"ifArray","hash":{},"fn":container.program(155, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n\n  <div class=\"row\">\n    <div class=\"grid\">\n\n"
    + ((stack1 = (helpers.ifArray || (depth0 && depth0.ifArray) || alias2).call(alias1,(depth0 != null ? depth0.arrest_security_type___1 : depth0),(depth0 != null ? depth0.arrest_security_type___2 : depth0),(depth0 != null ? depth0.arrest_security_type___3 : depth0),(depth0 != null ? depth0.arrest_security_type___4 : depth0),(depth0 != null ? depth0.arrest_security_type___5 : depth0),(depth0 != null ? depth0.arrest_security_type___6 : depth0),(depth0 != null ? depth0.arrest_security_type___7 : depth0),{"name":"ifArray","hash":{},"fn":container.program(157, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n\n"
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.security_arrest : depth0),{"name":"if","hash":{},"fn":container.program(159, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n\n\n\n"
    + ((stack1 = (helpers.ifArray || (depth0 && depth0.ifArray) || alias2).call(alias1,(depth0 != null ? depth0.killing_securityforcestype__1 : depth0),(depth0 != null ? depth0.killing_securityforcestype__2 : depth0),(depth0 != null ? depth0.killing_securityforcestype__3 : depth0),(depth0 != null ? depth0.killing_securityforcestype__4 : depth0),(depth0 != null ? depth0.killing_securityforcestype__5 : depth0),(depth0 != null ? depth0.killing_securityforcestype__6 : depth0),(depth0 != null ? depth0.killing_securityforcestype__7 : depth0),(depth0 != null ? depth0.killing_securityforcestype__8 : depth0),(depth0 != null ? depth0.killing_securityforces_oth : depth0),{"name":"ifArray","hash":{},"fn":container.program(178, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n"
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.security_killed : depth0),{"name":"if","hash":{},"fn":container.program(181, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n\n\n\n\n\n\n  </div>\n</div>\n\n\n\n"
    + ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || alias2).call(alias1,(depth0 != null ? depth0.security_officials_apprchd : depth0),9,{"name":"isnot","hash":{},"fn":container.program(199, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n  <div class=\"row\">\n    <div class=\"grid\">\n\n"
    + ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || alias2).call(alias1,(depth0 != null ? depth0.security_officials_apprchd : depth0),9,{"name":"isnot","hash":{},"fn":container.program(204, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n\n"
    + ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || alias2).call(alias1,(depth0 != null ? depth0.security_official_response__14 : depth0),1,{"name":"isnot","hash":{},"fn":container.program(210, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n"
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.court_or_commission : depth0),{"name":"if","hash":{},"fn":container.program(213, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n"
    + ((stack1 = (helpers.ifArray || (depth0 && depth0.ifArray) || alias2).call(alias1,(depth0 != null ? depth0.family_effects___1 : depth0),(depth0 != null ? depth0.family_effects___2 : depth0),(depth0 != null ? depth0.family_effects___3 : depth0),(depth0 != null ? depth0.family_effects___4 : depth0),(depth0 != null ? depth0.family_effects___5 : depth0),(depth0 != null ? depth0.family_effects___6 : depth0),(depth0 != null ? depth0.family_effects___7 : depth0),(depth0 != null ? depth0.family_effects___8 : depth0),(depth0 != null ? depth0.family_effects___9 : depth0),(depth0 != null ? depth0.family_effects___12 : depth0),(depth0 != null ? depth0.other_family_effects : depth0),{"name":"ifArray","hash":{},"fn":container.program(217, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n"
    + ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || alias2).call(alias1,(depth0 != null ? depth0.govnt_response_desired___11 : depth0),1,{"name":"isnot","hash":{},"fn":container.program(219, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n    </div>\n  </div>\n\n\n\n  <hr>  \n\n  <div class=\"row\">\n    <div class=\"col-sm-12\">\n      <h4>Related Victims</h4>\n    </div>\n  </div>\n\n\n"
    + ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || alias2).call(alias1,(depth0 != null ? depth0.number_of_victims : depth0),1,{"name":"isnot","hash":{},"fn":container.program(221, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n"
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.genuine_encounters : depth0),{"name":"if","hash":{},"fn":container.program(223, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n"
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.others_arrested : depth0),{"name":"if","hash":{},"fn":container.program(226, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n"
    + ((stack1 = (helpers.isnot || (depth0 && depth0.isnot) || alias2).call(alias1,(depth0 != null ? depth0.others_killed___9 : depth0),1,{"name":"isnot","hash":{},"fn":container.program(228, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n  <div class=\"row\">\n    <div class=\"col-sm-12\">\n      <p class=\"kicker\"><em><strong>Links to co-victim profiles forthcoming</strong></em></p>\n    </div>\n  </div>\n\n\n\n\n\n  <hr>  \n\n  <div class=\"row\">\n    <div class=\"col-sm-12\">\n      <h4>Reflections from the Family</h4>\n    </div>\n  </div>\n\n  <div class=\"row\">\n    <div class=\"col-sm-12\">\n      <p class=\"kicker\"><em><strong>Forthcoming</strong></em></p>\n    </div>\n  </div>\n\n\n"
    + ((stack1 = helpers["if"].call(alias1,(depth0 != null ? depth0.photo_doc_fn : depth0),{"name":"if","hash":{},"fn":container.program(231, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "\n\n";
},"useData":true});
})();