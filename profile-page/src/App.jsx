const chips = [
  "Machine Learning",
  "Distributed Systems",
  "Rust",
  "Python",
  "CUDA",
  "Data Visualization",
  "Technical Writing",
  "Mentorship",
];

const research = {
  lab: {
    title: "Undergraduate Research Assistant",
    lab: "Human-Centered AI Laboratory · Prof. Mira Kwon",
    period: "Sep 2023 – Present",
    bullets: [
      "Leading a sub-team studying interpretability of multimodal foundation models for clinical triage.",
      "Implemented active-learning pipelines with PyTorch, HuggingFace, and Ray Tune; reduced model drift by 18%.",
      "Coordinated with 4 graduate mentors to design participant studies and IRB protocols for explainable agents.",
    ],
  },
  publication: {
    title: "Adaptive Contrastive Explanations for Federated Diagnostics",
    venue: "NeurIPS Undergrad Spotlight · Nov 2024",
    summary:
      "Introduced a contrastive token-attribution framework improving clinician trust scores by 24% in simulation.",
    authors: "Park, E., Li, J., Kwon, M.",
  },
};

const experiences = [
  {
    title: "Software Engineering Intern",
    org: "Aether Robotics · Summer 2024",
    period: "12 weeks",
    bullets: [
      "Developed a vision-based calibration tool that reduced robot setup time by 35%.",
      "Implemented TypeScript tooling to auto-generate safety validation dashboards.",
    ],
  },
  {
    title: "Applied Research Intern",
    org: "Nimbus Cloud Intelligence · Summer 2023",
    period: "12 weeks",
    bullets: [
      "Prototyped anomaly detectors for streaming log data using Apache Flink & Rust.",
      "Published internal whitepaper on adaptive resource scaling for Kubernetes inference workloads.",
    ],
  },
  {
    title: "Part-Time Machine Learning Engineer",
    org: "Lumen Analytics Collective",
    period: "Jan 2024 – Jun 2024",
    bullets: [
      "Supported data quality automation while enrolled full-time; designed monitoring KPI suite in dbt.",
      "Delivered explainable churn models for non-profit partners, improving retention by 9%.",
    ],
  },
];

const projects = [
  {
    title: "Distributed Gradient Sandbox",
    context: "Parallel Computing · Rust, gRPC, CUDA",
    summary:
      "Built a modular experimentation toolkit for decentralized optimization; achieved 1.4× throughput against MPI baselines.",
  },
  {
    title: "CivicLens",
    context: "Human-Centered Computing · React, D3",
    summary:
      "Designed a visualization system translating municipal budgets into interpretable narratives; won Best Design Insight.",
  },
  {
    title: "BioSeq Tutor",
    context: "Computational Biology · Python, PyTorch",
    summary:
      "Implemented attention-based tutoring agents for sequencing labs with adaptive hints tied to protocol adherence.",
  },
  {
    title: "PolicyTrace",
    context: "Security Engineering · Go, Terraform",
    summary:
      "Delivered compliance-as-code prototypes validating IAM baselines across multi-cloud deployments, detecting 22 misconfigurations.",
  },
];

const certifications = [
  "AWS Certified Cloud Practitioner · 2024",
  "TensorFlow Developer Certificate · 2023",
  "IBM Data Science Professional · 2023",
  "Microsoft Azure AI Fundamentals · 2022",
];

const awards = [
  "1st place — Collegiate Computing Challenge 2024 for real-time data storytelling.",
  "Winner — ACM Student Research Competition (Regional, 2023) on interpretable AI.",
  "Grace Hopper Celebration Scholar (2023) · NCWIT Collegiate Award Finalist (2022).",
  "University Innovation Fellowship for advancing inclusive computing education.",
];

const chipClass =
  "inline-flex items-center rounded-full bg-slate-100 px-3 py-1 text-xs font-semibold text-slate-600 mr-2 mb-2";

const sectionCardClass =
  "bg-white shadow-lg rounded-2xl border border-slate-200 p-6 md:p-8";

export default function App() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100 text-slate-800 py-10 px-4">
      <div className="max-w-5xl mx-auto space-y-8">
        <header className={`${sectionCardClass} flex flex-col md:flex-row md:items-center md:justify-between gap-6`}>
          <div>
            <p className="uppercase tracking-[0.35em] text-xs text-indigo-500 font-semibold">
              PhD Applicant · Computer Science
            </p>
            <h1 className="text-4xl md:text-5xl font-bold text-slate-900 mt-2">
              Elena Park
            </h1>
            <p className="text-lg text-slate-600 mt-3 max-w-2xl">
              Bachelor of Science in Computer Science student passionate about high-performance computing, trustworthy AI, and human-centered systems. Seeking PhD opportunities to advance research in distributed learning and responsible automation.
            </p>
          </div>
          <div className="space-y-1 text-sm text-slate-600">
            <p className="font-semibold text-slate-800">elena.park@uni-example.edu</p>
            <p>(555) 123-7890 · Seattle, WA</p>
            <p>github.com/elenapark · linkedin.com/in/elenapark</p>
            <p>GPA: 3.92 / 4.00 · Expected Graduation: May 2026</p>
          </div>
        </header>

        <section className="grid md:grid-cols-2 gap-6">
          <article className={sectionCardClass}>
            <div className="flex items-center justify-between">
              <h2 className="text-xl font-semibold text-slate-900">Education</h2>
              <span className="text-sm text-indigo-600 font-semibold">Honors College</span>
            </div>
            <p className="mt-4 text-base font-semibold text-slate-800">
              Pacific Northwest University · B.S. Computer Science
            </p>
            <ul className="mt-3 list-disc list-inside text-sm text-slate-600 space-y-1">
              <li>Minor in Applied Mathematics · Dean&apos;s List (6×)</li>
              <li>Undergraduate AI Research Scholar · NSF Cyberinfrastructure Fellow</li>
              <li>Relevant Coursework: Distributed Systems, Statistical ML, Advanced Algorithms, Scientific Visualization</li>
            </ul>
          </article>
          <article className={sectionCardClass}>
            <h2 className="text-xl font-semibold text-slate-900">Core Strengths</h2>
            <div className="mt-4 flex flex-wrap">
              {chips.map((chip) => (
                <span key={chip} className={chipClass}>
                  {chip}
                </span>
              ))}
            </div>
          </article>
        </section>

        <section className={sectionCardClass}>
          <div className="flex items-center justify-between">
            <h2 className="text-2xl font-semibold text-slate-900">Research Experience</h2>
            <span className="text-xs uppercase tracking-[0.3em] text-slate-500">Lab · Publications</span>
          </div>
          <div className="mt-6 space-y-6">
            <article>
              <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-2">
                <div>
                  <p className="font-semibold text-lg text-slate-900">{research.lab.title}</p>
                  <p className="text-sm text-slate-500">{research.lab.lab}</p>
                </div>
                <span className="text-sm text-indigo-500 font-semibold">{research.lab.period}</span>
              </div>
              <ul className="mt-3 list-disc list-inside text-sm text-slate-600 space-y-1">
                {research.lab.bullets.map((bullet) => (
                  <li key={bullet}>{bullet}</li>
                ))}
              </ul>
            </article>
            <article className="border-t border-slate-200 pt-6">
              <p className="font-semibold text-lg text-slate-900">Publication</p>
              <p className="text-sm text-slate-500">{research.publication.venue}</p>
              <p className="mt-2 text-sm text-slate-600">
                {research.publication.authors}. “{research.publication.title}.” {research.publication.summary}
              </p>
            </article>
          </div>
        </section>

        <section className={sectionCardClass}>
          <div className="flex items-center justify-between">
            <h2 className="text-2xl font-semibold text-slate-900">Professional Experience</h2>
            <span className="text-xs uppercase tracking-[0.3em] text-slate-500">Internships · Part-Time</span>
          </div>
          <div className="mt-6 space-y-6">
            {experiences.map((exp) => (
              <article key={exp.title} className="border-t first:border-t-0 first:pt-0 border-slate-200 pt-6 first:pt-0">
                <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-2">
                  <div>
                    <p className="font-semibold text-lg text-slate-900">{exp.title}</p>
                    <p className="text-sm text-slate-500">{exp.org}</p>
                  </div>
                  <span className="text-sm text-indigo-500 font-semibold">{exp.period}</span>
                </div>
                <ul className="mt-3 list-disc list-inside text-sm text-slate-600 space-y-1">
                  {exp.bullets.map((bullet) => (
                    <li key={bullet}>{bullet}</li>
                  ))}
                </ul>
              </article>
            ))}
          </div>
        </section>

        <section className={sectionCardClass}>
          <div className="flex items-center justify-between">
            <h2 className="text-2xl font-semibold text-slate-900">Selected Projects</h2>
            <span className="text-xs uppercase tracking-[0.3em] text-slate-500">Coursework</span>
          </div>
          <div className="mt-6 grid md:grid-cols-2 gap-6">
            {projects.map((project) => (
              <article key={project.title} className="border border-slate-100 rounded-xl p-4 bg-slate-50">
                <p className="font-semibold text-lg text-slate-900">{project.title}</p>
                <p className="text-sm text-slate-500">{project.context}</p>
                <p className="mt-2 text-sm text-slate-600">{project.summary}</p>
              </article>
            ))}
          </div>
        </section>

        <section className="grid md:grid-cols-2 gap-6">
          <article className={sectionCardClass}>
            <h2 className="text-2xl font-semibold text-slate-900">Certifications</h2>
            <ul className="mt-4 space-y-3 text-sm text-slate-600">
              {certifications.map((cert) => (
                <li key={cert}>
                  <span className="font-semibold text-slate-800">{cert.split(" · ")[0]}</span> · {cert.split(" · ")[1]}
                </li>
              ))}
            </ul>
          </article>
          <article className={sectionCardClass}>
            <h2 className="text-2xl font-semibold text-slate-900">Awards & Honors</h2>
            <ul className="mt-4 space-y-3 text-sm text-slate-600">
              {awards.map((award) => (
                <li key={award}>{award}</li>
              ))}
            </ul>
          </article>
        </section>

        <footer className="text-center text-xs text-slate-500 py-6">
          © 2025 Elena Park · Open to PhD collaborations in trustworthy AI and systems research.
        </footer>
      </div>
    </div>
  );
}

