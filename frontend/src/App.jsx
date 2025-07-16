import './index.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom';

import LandingPage from './pages/LandingPage/LandingPage';
import AppLayout from './components/layout/AppLayout';

import Dashboard from './pages/Dashboard/Dashboard';
import AIModels from './pages/AIModels/AIModels';
import Compliance from './pages/Compliance/Compliance';
import Reports from './pages/Reports/Reports';
import Settings from './pages/Settings/Settings';

function App() {
  return (
    <BrowserRouter>
      <Routes>

        {/* Landing page (publique) */}
        <Route path="/" element={<LandingPage />} />

        {/* Pages internes avec layout global */}
        // 🔗 Lien entre les routes internes et le layout global (AppLayout)
        <Route element={<AppLayout />}>
          <Route path="/Dashboard" element={<Dashboard />} />
          <Route path="/AIModels" element={<AIModels />} />
          <Route path="/Compliance" element={<Compliance />} />
          <Route path="/Reports" element={<Reports />} />
          <Route path="/Settings" element={<Settings />} />
        </Route>

      </Routes>
    </BrowserRouter>
  );
}

export default App;
