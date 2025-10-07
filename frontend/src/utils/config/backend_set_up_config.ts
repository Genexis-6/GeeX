

export class BackendSetUpConfig {
    static domain: string = "http://127.0.0.1";
    static port: number = 9000;
    static apiVersion: string = "v1";
    static pDomain:string = "https://gpayment-api.onrender.com/"

    static backendUrl: string = `${BackendSetUpConfig.domain}:${BackendSetUpConfig.port}/${BackendSetUpConfig.apiVersion}`;
    static prototypeUrl:string = `${BackendSetUpConfig.pDomain}${BackendSetUpConfig.apiVersion}`



}


