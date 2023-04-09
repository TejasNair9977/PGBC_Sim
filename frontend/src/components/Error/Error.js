import classes from'./Error.module.css'
import { Link } from 'react-router-dom'
const Error = () => {
    return (
        <>
        <div className={classes.wrapper}>
        <div className={classes.c}>
                <div className={classes._404}>404</div>
                <div className={classes.hr}></div>
                    <div className={classes._1}>THE PAGE</div>
                    <div className={classes._2}>WAS NOT FOUND</div>
                    <Link to ="/" className={classes.btn} >BACK TO HOME</Link>
            </div>
        </div>
            
        </>
    )
}
export default Error