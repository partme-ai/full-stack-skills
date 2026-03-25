---
name: spring-security
description: "Provides comprehensive guidance for Spring Security including authentication, authorization, OAuth2, JWT, and security best practices. Use when the user asks about Spring Security, needs to implement security in Spring applications, configure authentication, or work with security features."
license: Complete terms in LICENSE.txt
---

## When to use this skill

Use this skill whenever the user wants to:
- Configure authentication and authorization in Spring Boot applications
- Set up SecurityFilterChain, UserDetailsService, and PasswordEncoder
- Implement JWT-based stateless authentication
- Integrate OAuth2 client or resource server
- Use method-level security with @PreAuthorize and @Secured
- Configure CORS, CSRF, session management, and security headers

## How to use this skill

### Workflow

1. **Add the Spring Security starter** dependency
2. **Configure SecurityFilterChain** to define URL-based access rules
3. **Implement authentication**: in-memory, JDBC, LDAP, or custom UserDetailsService
4. **Add authorization**: role-based or expression-based access control

### 1. Basic Security Configuration

```java
@Configuration
@EnableWebSecurity
public class SecurityConfig {

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .authorizeHttpRequests(auth -> auth
                .requestMatchers("/api/public/**").permitAll()
                .requestMatchers("/api/admin/**").hasRole("ADMIN")
                .anyRequest().authenticated()
            )
            .httpBasic(Customizer.withDefaults());
        return http.build();
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
}
```

### 2. Custom UserDetailsService

```java
@Service
public class CustomUserDetailsService implements UserDetailsService {
    private final UserRepository userRepository;

    public CustomUserDetailsService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    @Override
    public UserDetails loadUserByUsername(String username) {
        User user = userRepository.findByUsername(username)
            .orElseThrow(() -> new UsernameNotFoundException("User not found: " + username));
        return new org.springframework.security.core.userdetails.User(
            user.getUsername(), user.getPassword(), user.getAuthorities()
        );
    }
}
```

### 3. JWT Authentication Filter

```java
@Component
public class JwtAuthFilter extends OncePerRequestFilter {
    private final JwtService jwtService;
    private final UserDetailsService userDetailsService;

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain chain)
            throws ServletException, IOException {
        String token = extractToken(request);
        if (token != null && jwtService.isValid(token)) {
            String username = jwtService.extractUsername(token);
            UserDetails userDetails = userDetailsService.loadUserByUsername(username);
            var authToken = new UsernamePasswordAuthenticationToken(userDetails, null, userDetails.getAuthorities());
            SecurityContextHolder.getContext().setAuthentication(authToken);
        }
        chain.doFilter(request, response);
    }
}
```

### 4. Method-Level Security

```java
@EnableMethodSecurity
@Configuration
public class MethodSecurityConfig {}

@Service
public class AdminService {
    @PreAuthorize("hasRole('ADMIN')")
    public void deleteUser(Long id) { /* ... */ }

    @PreAuthorize("#userId == authentication.principal.id")
    public UserProfile getProfile(Long userId) { /* ... */ }
}
```

## Best Practices

- Always encode passwords with BCrypt or Argon2; never store plaintext passwords
- Use HTTPS in production; configure security headers (HSTS, X-Content-Type-Options)
- Apply the principle of least privilege; design roles and permissions carefully
- Protect sensitive endpoints; use CSRF protection for browser-based applications
- Configure CORS explicitly for API servers

## Resources

- Official reference: https://docs.spring.io/spring-security/reference/
- Spring Security samples: https://github.com/spring-projects/spring-security-samples

## Keywords

spring security, authentication, authorization, JWT, OAuth2, SecurityFilterChain, UserDetailsService, BCrypt, CORS, CSRF, method security, PreAuthorize, roles, permissions
