export interface BackendApiRes<TRes> {
    statusCode: number,
    message: string,
    data?: TRes
}