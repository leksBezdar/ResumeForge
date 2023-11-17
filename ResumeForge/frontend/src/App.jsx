import { Route, Routes } from 'react-router-dom'
import ResumeForm from "./components/ResumeForm"

export default function App() {
	return (
		<>
			<Routes>
				<Route path='/resume_form' element={<ResumeForm />} />
			</Routes>
		</>
	)
} 