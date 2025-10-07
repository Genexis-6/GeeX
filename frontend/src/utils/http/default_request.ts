import type { getRequestArgs, postRequestArgs } from "./request_args";

export class DefaultRequest {

    // default api commincations
    static async post<TModel, TRes>({ url, contentType = "application/json", token = "", payload }: postRequestArgs<TModel>): Promise<TRes> {
        try {
            let response: Response = await fetch(url, {
                method: "POST",
                credentials: "include",
                headers: DefaultRequest.requestHeaderType({ token: token, contentType }),
                body: JSON.stringify(payload)
            })
            const data = (await response.json()) as TRes;
            return {
                ...(data as object),
                statusCode: (data as any).status_code ?? response.status
            } as TRes;
        } catch (error) {
            console.error("error communicating with server due to", error)
            throw error

        }
    }

    static async get<TRes>({ url, contentType = "application/json", token = "" }: getRequestArgs): Promise<TRes> {
        try {
            let response: Response = await fetch(url, {
                method: "POST",
                credentials: "include",
                headers: DefaultRequest.requestHeaderType({ token: token, contentType }),

            })
            const data: TRes = await response.json()
            return {
                ...(data as object),
                statusCode: (data as any).status_code ?? response.status
            } as TRes;
        } catch (error) {
            console.error("error communicating with server due to", error)
            throw error

        }


    }


    static requestHeaderType({ token, contentType }: { token: string, contentType: string }): Record<string, string> {
        return token.trim() == "" ? {
            "content-type": contentType
        } : {
            "content-type": contentType,
            "authorization": `Bearer ${token}`
        }
    }


}