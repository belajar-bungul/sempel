import { registry } from "@web/core/registry";
export const samReloadService = {
    dependencies: ["bus_service"],
    start(env, { bus_service }) {
        let reloading = false;
        bus_service.subscribe("sam_reload", () => {
            if (!reloading) {
                reloading = true;
                window.location.reload();
            }
        });
        bus_service.start();
    },
};

registry.category("services").add("sam_reload", samReloadService);
