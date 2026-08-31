import { patch } from "@web/core/utils/patch";
import { Chatter } from "@mail/chatter/web_portal/chatter";
import { session } from "@web/session";

patch(Chatter.prototype, {
    samAllow(kind) {
        const rules = (session.sam && session.sam.chatter) || {};
        const modelRules = rules[this.props.threadModel] || rules["*"];
        if (!modelRules) {
            return true;
        }
        return !modelRules[kind];
    },
});
