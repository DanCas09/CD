
import java.util.StringTokenizer;
import java.util.GregorianCalendar;
import java.util.Calendar;

import oursource.comparacoes.*; 

/**
   Classe Pessoa.
   Esta classe implementa a interface Serializable de forma a
   permitir escrever instancias suas em ficheiro. 
 */
public class Person implements java.io.Serializable, Comparable  {
      
   /* Atributos que nao podem variar numa pessoa. */
   private String name;
   private Calendar birthDay;
   /* Atributos susceptiveis de serem alterados.  */  
   private String address;
   private Contact contact;       

  /**
      Classe interna para implementar o criterio alternativo 
      de comparacao por idades.
   */ 
   public static class CompareByAge extends Compare {       

      public int compare( Object firstObject, Object secondObject ) {
         /* Obter as datas de nascimento das duas pessoas. */
         Calendar firstDate = ((Person)firstObject).getBirthDay();           
         Calendar secondDate = ((Person)secondObject).getBirthDay();           
               
         /* Testar a data mais recente. */
         if(firstDate.after(secondDate)) 
            /* Uma data mais recente e maior que uma data anterior. */
            return CompareConstants.BIGGER;
         return CompareConstants.SMALLER;
      }
   }  

  /**
      Metodo estatico privado que compara dois nomes independentemente 
      do numero de espacos brancos entres os nomes,
   */
   private static boolean compareNames( String nameFirstPerson, String nameSecondPerson ) {              

      /* Criar os Tokenizer's com o separador "  " */
      StringTokenizer st1 = new StringTokenizer(nameFirstPerson,"  ");
      StringTokenizer st2 = new StringTokenizer(nameSecondPerson,"  ");                
                
      /* Se nao tem o mesmo numero de "nomes", entao sao 
         nomes de pessoas diferentes. */
      if(st1.countTokens()!=st2.countTokens())
         return false;

      /* Ambas os nomes completos tem o mesmo numero de "nomes". */
      /* Comparar os sucessivos "nomes" (tokens).  */
      while (st1.hasMoreTokens() && st2.hasMoreTokens()) {
         if(st1.nextToken().equalsIgnoreCase(st2.nextToken())==false )
            return false;
      }                     
      /* Todos os nomes parciais sao iguais, logo trata-se da mesma pessoa. */
      return true;                        
   }

  /** 
      Construtor para iniciar um objecto Person.
   */
   public Person( String fullName, Calendar birthDay, String address, Contact contact ) {

      this.name = fullName; 
      this.birthDay  = birthDay;
      this.address   = address;
      this.contact = contact;
   }

  /**
      Obter o primeiro nome.
   */
   public String getFirstName()   { 
      /* Criar o Tokenizer com o separador "  " sobre o nome. */
      StringTokenizer st = new StringTokenizer(name," ");
      /* O primeiro token e o primeiro nome da pessoa. */
      return st.nextToken();
   }                

  /**
      Obter o ultimo nome.
   */
   public String getLastName()    {       
      /* Criar o Tokenizer com o separador " " sobre o nome. */
      StringTokenizer st = new StringTokenizer(name,"  ");
      /* Verificar o numero de nomes. */                
      if(st.countTokens()==1) return "";
      /* Avancar os tokens ate ao penultimo */                                
      while (st.countTokens()>1) 
         st.nextToken();
      /* O ultimo token e o ultimo nome (apelido) da pessoa. */
      return st.nextToken();
   }
        
  /**
      Obter o nome completo.
   */
   public String getFullName()   { return name; }        

  /**
      Obter a data de nascimento.
   */
   public Calendar getBirthDay() {  return birthDay;   }

  /**
      Obter o endereco.
   */
   public String getAddress()     { return address;     }

  /**
      Obter os contactos.
   */
   public Contact getContact() { return contact; }

   // Metodos para alterar os atributos da pessoa.
   
  /**
      Alterar a data de nascimento.
   */
   public void setBirthDay( Calendar newBirthDay) {  birthDay = newBirthDay;  }

  /**
      Alterar a morada.
   */
   public void setAddress(String newAddress) { address = newAddress;  }

  /**
      Alterar os contactos.
   */
   public void setContact(Contact newContact) { contact = newContact; }        
      
  /**
      Construir uma String com os campos que descrevem a pessoa.
   */ 
   public String toString() {
      return getFirstName() +' '+ getLastName();
   }

  /**
      Comparar com outro objecto Pessoa.
      O criterio de comparacao de o primeiro nome.
      Tem que se garantir que o objecto passado como parametro e uma instancia da 
      classe Person. Caso contrario de um erro de programacao.
   */
   public int compare( Comparable person )  {

      if( getFirstName().compareTo( ((Person)person).getFirstName() ) <0 )
         /* O nome do "this" e alfabeticamente inferior. */
         return CompareConstants.SMALLER;
      /* O nome do "this" e alfabeticamente superior ou igual. */
      return CompareConstants.BIGGER;
   }
        
  /**
      Verificar se duas pessoas sao a mesma.
      A comparacao tem como base os campos que definem univocamente a pessoa:
      - Nome.
      - Data de nascimento.
   */
   public boolean equals( Object object )  {
      if(object==null)
         /* O objecto "this" nao e "null". */
         return false;
               
      if( (object instanceof Person) == false ) 
         /* O objecto passado como parametro nao e uma instancia da classe Person. */   
         return false;   

      /* Efectuar a comparacao dos objectos. */
      if(this==object) 
         /* "this" e "object" referem o mesmo objecto. */
         return true;
                
      /* Comparar apenas os atributos que definem univocamente uma pessoa. */                           
      if( compareNames(name,((Person)object).name) == true ) {
         if(birthDay.equals(((Person)object).birthDay)) 
            /* Trata-se da mesma pessoa. */  
            return true;
      }
      /* Sao pessoas diferentes. */                        
      return false;
   }

  /**
      Obter um objecto que implementa o criterio de comparacao por idade.
   */
   public static Compare getByAgeCriteria() {
      return new CompareByAge();
   }
}  /* Fim da classe Person */

