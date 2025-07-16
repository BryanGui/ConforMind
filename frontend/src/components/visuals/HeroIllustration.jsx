export default function HeroIllustration(props) {
  return (
    <svg
      viewBox="0 0 500 300"
      xmlns="http://www.w3.org/2000/svg"
      className={props.className}
    >
      <defs>
        <linearGradient id="grad" x1="0%" y1="0%" x2="100%" y2="100%">
          <stop offset="0%" stopColor="#6366f1" />
          <stop offset="100%" stopColor="#06b6d4" />
        </linearGradient>
      </defs>
      <rect x="30" y="30" width="440" height="240" rx="20" fill="#1e1e2f" />
      <rect x="60" y="70" width="380" height="30" rx="6" fill="url(#grad)" />
      <rect x="60" y="120" width="300" height="20" rx="4" fill="#2dd4bf" />
      <rect x="60" y="160" width="200" height="20" rx="4" fill="#94a3b8" />
      <circle cx="450" cy="200" r="18" fill="#22d3ee" />
      <circle cx="450" cy="200" r="10" fill="white" opacity="0.2" />
      <text x="60" y="250" fill="#94a3b8" fontSize="14" fontFamily="sans-serif">
        Aperçu de conformité
      </text>
    </svg>
  );
}
