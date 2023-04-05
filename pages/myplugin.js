(function () {
  class MyPlugin {
    install() {}
    configure(pluginManager) {
      pluginManager.jexl.addFunction("colorFeature", (feature) => {
        let name = feature.get("name");
        if (name === "inv_h2") {
          return "red";
        } else if (type === "del_hom") {
          return "green";
        } else {
          return "purple";
        }
      });
    }
  }

  // the plugin will be included in both the main thread and web worker, so
  // install plugin to either window or self (webworker global scope)
  (typeof self !== "undefined" ? self : window).JBrowsePluginMyPlugin = {
    default: Plugin,
  };
})();
