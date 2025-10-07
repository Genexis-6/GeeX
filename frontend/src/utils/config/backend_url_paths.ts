import { BackendSetUpConfig } from "./backend_set_up_config";

export class BackendUrlPaths{

    // auth urls
    static registration:string = `${BackendSetUpConfig.backendUrl}\\auth\\register`
    static regprototype:string = `${BackendSetUpConfig.prototypeUrl}\\hanauth\\register`
}