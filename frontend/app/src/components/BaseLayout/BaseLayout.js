import LoadingPage from "./components/LoadingPage/LoadingPage";
import './BaseLayout.css'

function BaseLayout() {
    return(
        <div className="base">
            <div className="base_page-wrapper">
                <LoadingPage />
            </div>
        </div>
    );
}

export default BaseLayout