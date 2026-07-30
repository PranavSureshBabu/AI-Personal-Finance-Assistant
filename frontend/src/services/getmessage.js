import api from "./api";

export async function getMessage() {
    const response = await api.get("/");
    return response.data;
}