import { dateNavbar } from './dateNavBar'
import NavBar from './NavBar'
import './NavBarLists.css'
import logo from '../../../assets/media/logo.svg'

const NavBarList = () => {
  return (
    <div className='navbar__container'>

      <div className='navbar-logo'>
        <img src={logo} alt="logo" />
      </div>

      <div className='navbar__content'>
        {dateNavbar.map(item => (
          <NavBar key={item.id} navbar={item} />
        ))}
      </div>
    </div>
  )
}

export default NavBarList