export type postRequestArgs<T> = {
    url: string,
    contentType?: string,
    payload: T,
    token?: string,

}

export type getRequestArgs = {
    url:string,
    contentType:string,
    token?:string
}

