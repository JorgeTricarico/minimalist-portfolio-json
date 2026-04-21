import { describe, it, expect } from 'vitest';
import { applySmartBolding, getSection, mapYamlToJson, cvSchema } from './yaml_to_json.js';

describe('YAML to JSON Converter', () => {

  describe('applySmartBolding', () => {
    it('should apply bold to valid keywords', () => {
      const text = "I am an expert in Python and AI";
      const keywords = ["Python", "AI"];
      const result = applySmartBolding(text, keywords);
      expect(result).toBe("I am an expert in <strong>Python</strong> and <strong>AI</strong>");
    });

    it('should ignore case but keep original case', () => {
      const text = "Testing python and AI";
      const keywords = ["Python", "AI"];
      const result = applySmartBolding(text, keywords);
      expect(result).toBe("Testing <strong>python</strong> and <strong>AI</strong>");
    });
    
    it('should handle undefined or empty text/keywords', () => {
      expect(applySmartBolding("", ["Python"])).toBe("");
      expect(applySmartBolding("test", [])).toBe("test");
    });
  });

  describe('getSection', () => {
    it('should return the correct section from alternative names', () => {
      const sections = {
        Educación: [{ institution: "UBA" }]
      };
      
      const result = getSection(sections, ['Educacion', 'Educación', 'Education']);
      expect(result).toEqual([{ institution: "UBA" }]);
    });
    
    it('should return null if section does not exist', () => {
      const sections = {
        Otros: []
      };
      const result = getSection(sections, ['Educacion', 'Educación', 'Education']);
      expect(result).toBeNull();
    });
  });

  describe('mapYamlToJson', () => {
    it('should successfully map and validate a valid CV object', () => {
      const mockCvData = {
        cv: {
          name: "John Doe",
          email: "john@example.com",
          phone: "123456",
          website: "https://john.com",
          location: "Buenos Aires, Argentina",
          social_networks: [
            { network: "LinkedIn", username: "johndoe" }
          ],
          sections: {
            Resumen: ["Here is a short summary text."],
            Experiencia: [
              { company: "Tech Inc", position: "Dev", start_date: "2020-01", end_date: "present", highlights: ["Did things"] }
            ],
            Educación: [
              { institution: "University", degree: "BSc", area: "CS", start_date: "2015-01", end_date: "2019-12" }
            ],
            Habilidades: [
              { label: "Programming", details: "JavaScript, TypeScript" }
            ]
          }
        },
        settings: {
          bold_keywords: ["summary"] // Should bold summary in the resumen
        }
      };

      const result = mapYamlToJson(mockCvData);

      expect(result).toBeDefined();
      expect(result.basics.name).toBe("John Doe");
      expect(result.basics.summary).toContain("<strong>summary</strong>");
      expect(result.work.length).toBe(1);
      expect(result.work[0].startDate).toBe("2020-01-01"); // appended "-01"
      expect(result.work[0].endDate).toBeNull(); // "present" parsed to null
      expect(result.education.length).toBe(1);
      expect(result.skills[0].keywords).toEqual(["JavaScript", "TypeScript"]);
      
      // Should correctly validate the parsed schema format
      expect(() => cvSchema.parse(result)).not.toThrow();
    });

    it('should throw an error if input has no cv structure', () => {
      expect(() => mapYamlToJson({})).toThrow('El archivo cv.yaml o la data carece de formato RenderCV.');
    });

    it('should throw a zod error if data is fundamentally invalid/missing types', () => {
      const invalidCvData = {
        cv: {
          name: 123, // Invalid: should be a string
          sections: {}
        }
      };
      
      expect(() => mapYamlToJson(invalidCvData)).toThrow(); // Zod error should be thrown
    });
  });

});
