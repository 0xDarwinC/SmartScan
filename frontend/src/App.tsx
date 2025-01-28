import * as React from "react";  
import Router from "./router";  
  
function App() {
    const { user } = useUser();
    const { loading, loginError } = useAuthenticate();
    
    if (loginError) {
        return (
            <h5 className="text-semibold mt-5 text-center">
                Unable to sign in. Please try again.
            </h5>
        );
    }

    if (loading) {
        return <h5 className="text-semibold mt-5 text-center">Signing in...</h5>
    }

    if (!user) {
        return (
            <h5 className="text-semibold mt-5 text-center">
                Restricted access. Please sign in to continue. 
            </h5>
        );
    }
    return <Router />;
}
export default App;