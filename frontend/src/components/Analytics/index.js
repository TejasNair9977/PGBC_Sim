import './index.scss'
import TuplesReturned from '../TuplesReturned'
import TuplesFetched from '../TuplesFetched'
import TuplesInserted from '../TuplesInserted'
import TuplesUpdated from '../TuplesUpdated'
import TuplesDeleted from '../TuplesDeleted'

const Analytics = () => {
  return (
    <div className='Analytics-container'>
        <div className='square-box'>
          <TuplesReturned />
        </div>
        <div className='square-box'>
          <TuplesFetched />
        </div>
        <div className='square-box'>
          <TuplesInserted />
        </div>
        <div className='square-box'>
          <TuplesUpdated />
        </div>
        <div className='square-box'>
          <TuplesDeleted />
        </div>
    </div>
  )
}

export default Analytics
