type buttonParams = {
    title: string,
    operation: ()=>void,
    disabled?: boolean
}



export default function DefaultButton({
    title, operation, disabled = false
}: buttonParams) {
    return <button
        onClick={() => operation}
        disabled={disabled}
        className="default-button">
        {title}
    </button>
}